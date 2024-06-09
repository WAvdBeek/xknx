"""
Device is the base class for all implemented devices (e.g. Lights/Switches/Sensors).

It provides basis functionality for reading the state from the KNX bus.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
import asyncio
from collections.abc import Callable, Coroutine, Iterator
import logging
from typing import TYPE_CHECKING, Any, TypeVar

from xknx.remote_value import RemoteValue
from xknx.telegram import Telegram
from xknx.telegram.address import DeviceGroupAddress
from xknx.telegram.apci import GroupValueRead, GroupValueResponse, GroupValueWrite

if TYPE_CHECKING:
    from xknx.xknx import XKNX

T = TypeVar("T", bound="Device")
DeviceCallbackType = Callable[[T], Coroutine[Any, Any, None]]

logger = logging.getLogger("xknx.log")


class Device(ABC):
    """Base class for devices."""

    def __init__(
        self: T,
        xknx: XKNX,
        name: str,
        device_updated_cb: DeviceCallbackType[T] | None = None,
    ):
        """Initialize Device class."""
        self.xknx = xknx
        self.name = name
        self.device_updated_cbs: list[DeviceCallbackType[T]] = []
        if device_updated_cb is not None:
            self.register_device_updated_cb(device_updated_cb)

    def register_state_updater(self) -> None:
        """Register device addresses for StateUpdater."""
        for remote_value in self._iter_remote_values():
            remote_value.register_state_updater()

    def unregister_state_updater(self) -> None:
        """Unregister device addresses from StateUpdater."""
        for remote_value in self._iter_remote_values():
            remote_value.unregister_state_updater()

    def async_start_tasks(self) -> None:
        """Start async background tasks of device."""
        return

    def async_remove_tasks(self) -> None:
        """Remove all tasks of device."""
        return

    @abstractmethod
    def _iter_remote_values(self) -> Iterator[RemoteValue[Any]]:
        """Iterate the devices RemoteValue classes."""
        # yield self.remote_value
        # yield from (<list all used RemoteValue instances>)
        yield from ()

    def register_device_updated_cb(
        self: T, device_updated_cb: DeviceCallbackType[T]
    ) -> None:
        """Register device updated callback."""
        self.device_updated_cbs.append(device_updated_cb)

    def unregister_device_updated_cb(
        self: T, device_updated_cb: DeviceCallbackType[T]
    ) -> None:
        """Unregister device updated callback."""
        if device_updated_cb in self.device_updated_cbs:
            self.device_updated_cbs.remove(device_updated_cb)

    async def after_update(self: T) -> None:
        """Execute callbacks after internal state has been changed."""
        try:
            await asyncio.gather(*[cb(self) for cb in self.device_updated_cbs])
        except Exception:  # pylint: disable=broad-except
            logger.exception(
                "Unexpected error while processing device_updated_cb for %s",
                self,
            )

    async def sync(self, wait_for_result: bool = False) -> None:
        """Read states of device from KNX bus."""
        for remote_value in self._iter_remote_values():
            await remote_value.read_state(wait_for_result=wait_for_result)

    async def process(self, telegram: Telegram) -> None:
        """Process incoming telegram."""
        if isinstance(telegram.payload, GroupValueWrite):
            await self.process_group_write(telegram)
        elif isinstance(telegram.payload, GroupValueResponse):
            await self.process_group_response(telegram)
        elif isinstance(telegram.payload, GroupValueRead):
            await self.process_group_read(telegram)

    async def process_group_read(self, telegram: Telegram) -> None:
        """Process incoming GroupValueRead telegrams."""
        # The default is, that devices don't answer to group reads
        return

    async def process_group_response(self, telegram: Telegram) -> None:
        """Process incoming GroupValueResponse telegrams."""
        # Per default mapped to group write.
        await self.process_group_write(telegram)

    async def process_group_write(self, telegram: Telegram) -> None:
        """Process incoming GroupValueWrite telegrams."""
        # The default is, that devices don't process group writes
        return

    def get_name(self) -> str:
        """Return name of device."""
        return self.name

    def has_group_address(self, group_address: DeviceGroupAddress) -> bool:
        """Test if device has given group address."""
        return any(
            remote_value.has_group_address(group_address)
            for remote_value in self._iter_remote_values()
        )

    def __eq__(self, other: object) -> bool:
        """Compare for quality."""
        return self.__dict__ == other.__dict__

"""Test DPT lookup."""

# flake8: noqa
import pytest

from xknx.dpt import *

# """
# Generate a list of all DPTs for the following test.
# Run this function manually to update the list.
# """

# dpt_dict = {}
# for dpt in DPTBase.dpt_class_tree():
#     if dpt.value_type is not None:
#         dpt_dict[dpt.value_type] = dpt

# for _, dpt in sorted(dpt_dict.items()):
#     unit = None
#     if dpt.unit is not None:
#         unit = f'"{dpt.unit}"'
#     print(
#         f'("{dpt.value_type}", {dpt.__name__}, {dpt.dpt_main_number}, {dpt.dpt_sub_number}, {unit}),'
#     )


@pytest.mark.parametrize(
    "value_type,dpt_class,main,sub,unit",
    [
        ("1byte_signed", DPTSignedRelativeValue, 6, None, None),
        ("1byte_unsigned", DPTValue1ByteUnsigned, 5, None, None),
        ("2byte_float", DPT2ByteFloat, 9, None, None),
        ("2byte_signed", DPT2ByteSigned, 8, None, None),
        ("2byte_unsigned", DPT2ByteUnsigned, 7, None, None),
        ("4byte_float", DPT4ByteFloat, 14, None, None),
        ("4byte_signed", DPT4ByteSigned, 13, None, None),
        ("4byte_unsigned", DPT4ByteUnsigned, 12, None, None),
        ("absolute_humidity", DPTAbsoluteHumidity, 9, 29, "g/m³"),
        ("absolute_temperature", DPTAbsoluteTemperature, 14, 69, "K"),
        ("acceleration", DPTAcceleration, 14, 0, "m/s²"),
        ("acceleration_angular", DPTAccelerationAngular, 14, 1, "rad/s²"),
        ("activation_energy", DPTActivationEnergy, 14, 2, "J/mol"),
        ("active_energy", DPTActiveEnergy, 13, 10, "Wh"),
        ("active_energy_kwh", DPTActiveEnergykWh, 13, 13, "kWh"),
        ("active_energy_mwh", DPTActiveEnergyMWh, 13, 16, "MWh"),
        ("activity", DPTActivity, 14, 3, "s⁻¹"),
        ("air_flow", DPTAirFlow, 9, 9, "m³/h"),
        ("amplitude", DPTAmplitude, 14, 5, None),
        ("angle", DPTAngle, 5, 3, "°"),
        ("angle_deg", DPTAngleDeg, 14, 7, "°"),
        ("angle_rad", DPTAngleRad, 14, 6, "rad"),
        ("angular_frequency", DPTAngularFrequency, 14, 34, "rad/s"),
        ("angular_momentum", DPTAngularMomentum, 14, 8, "J s"),
        ("angular_velocity", DPTAngularVelocity, 14, 9, "rad/s"),
        ("apparant_energy", DPTApparantEnergy, 13, 11, "VAh"),
        ("apparant_energy_kvah", DPTApparantEnergykVAh, 13, 14, "kVAh"),
        ("apparent_power", DPTApparentPower, 14, 80, "VA"),
        ("area", DPTArea, 14, 10, "m²"),
        ("brightness", DPTBrightness, 7, 13, "lx"),
        ("capacitance", DPTCapacitance, 14, 11, "F"),
        ("charge_density_surface", DPTChargeDensitySurface, 14, 12, "C/m²"),
        ("charge_density_volume", DPTChargeDensityVolume, 14, 13, "C/m³"),
        ("color_temperature", DPTColorTemperature, 7, 600, "K"),
        ("common_temperature", DPTCommonTemperature, 14, 68, "°C"),
        ("compressibility", DPTCompressibility, 14, 14, "m²/N"),
        ("concentration_ugm3", DPTConcentrationUGM3, 9, 30, "μg/m³"),
        ("conductance", DPTConductance, 14, 15, "S"),
        ("counter_pulses", DPTValue1Count, 6, 10, "counter pulses"),
        ("curr", DPTCurrent, 9, 21, "mA"),
        ("current", DPTUElCurrentmA, 7, 12, "mA"),
        ("decimal_factor", DPTDecimalFactor, 5, 5, None),
        ("delta_time_100ms", DPTDeltaTime100Msec, 8, 4, "ms"),
        ("delta_time_10ms", DPTDeltaTime10Msec, 8, 3, "ms"),
        ("delta_time_hrs", DPTDeltaTimeHrs, 8, 7, "h"),
        ("delta_time_min", DPTDeltaTimeMin, 8, 6, "min"),
        ("delta_time_ms", DPTDeltaTimeMsec, 8, 2, "ms"),
        ("delta_time_sec", DPTDeltaTimeSec, 8, 5, "s"),
        ("density", DPTDensity, 14, 17, "kg/m³"),
        ("electric_charge", DPTElectricCharge, 14, 18, "C"),
        ("electric_current", DPTElectricCurrent, 14, 19, "A"),
        ("electric_current_density", DPTElectricCurrentDensity, 14, 20, "A/m²"),
        ("electric_dipole_moment", DPTElectricDipoleMoment, 14, 21, "C m"),
        ("electric_displacement", DPTElectricDisplacement, 14, 22, "C/m²"),
        ("electric_field_strength", DPTElectricFieldStrength, 14, 23, "V/m"),
        ("electric_flux", DPTElectricFlux, 14, 24, "c"),
        ("electric_flux_density", DPTElectricFluxDensity, 14, 25, "C/m²"),
        ("electric_polarization", DPTElectricPolarization, 14, 26, "C/m²"),
        ("electric_potential", DPTElectricPotential, 14, 27, "V"),
        ("electric_potential_difference", DPTElectricPotentialDifference, 14, 28, "V"),
        ("electrical_conductivity", DPTElectricalConductivity, 14, 16, "S/m"),
        ("electromagnetic_moment", DPTElectromagneticMoment, 14, 29, "A m²"),
        ("electromotive_force", DPTElectromotiveForce, 14, 30, "V"),
        ("energy", DPTEnergy, 14, 31, "J"),
        ("enthalpy", DPTEnthalpy, 9, 60000, "H"),
        ("flow_rate_m3h", DPTFlowRateM3H, 13, 2, "m³/h"),
        ("force", DPTForce, 14, 32, "N"),
        ("frequency", DPTFrequency, 14, 33, "Hz"),
        ("heat_quantity", DPTHeatQuantity, 14, 37, "J"),
        ("heatcapacity", DPTHeatCapacity, 14, 35, "J/K"),
        ("heatflowrate", DPTHeatFlowRate, 14, 36, "W"),
        ("humidity", DPTHumidity, 9, 7, "%"),
        ("illuminance", DPTLux, 9, 4, "lx"),
        ("impedance", DPTImpedance, 14, 38, "Ω"),
        ("kelvin_per_percent", DPTKelvinPerPercent, 9, 23, "K/%"),
        ("latin_1", DPTLatin1, 16, 1, None),
        ("length", DPTLength, 14, 39, "m"),
        ("length_m", DPTLengthM, 8, 12, "m"),
        ("length_mm", DPTLengthMm, 7, 11, "mm"),
        ("light_quantity", DPTLightQuantity, 14, 40, "lm s"),
        ("long_delta_timesec", DPTLongDeltaTimeSec, 13, 100, "s"),
        ("long_time_period_hrs", DPTLongTimePeriodHrs, 12, 102, "h"),
        ("long_time_period_min", DPTLongTimePeriodMin, 12, 101, "min"),
        ("long_time_period_sec", DPTLongTimePeriodSec, 12, 100, "s"),
        ("luminance", DPTLuminance, 14, 41, "cd/m²"),
        ("luminous_flux", DPTLuminousFlux, 14, 42, "lm"),
        ("luminous_intensity", DPTLuminousIntensity, 14, 43, "cd"),
        ("magnetic_field_strength", DPTMagneticFieldStrength, 14, 44, "A/m"),
        ("magnetic_flux", DPTMagneticFlux, 14, 45, "Wb"),
        ("magnetic_flux_density", DPTMagneticFluxDensity, 14, 46, "T"),
        ("magnetic_moment", DPTMagneticMoment, 14, 47, "A m²"),
        ("magnetic_polarization", DPTMagneticPolarization, 14, 48, "T"),
        ("magnetization", DPTMagnetization, 14, 49, "A/m"),
        ("magnetomotive_force", DPTMagnetomotiveForce, 14, 50, "A"),
        ("mass", DPTMass, 14, 51, "kg"),
        ("mass_flux", DPTMassFlux, 14, 52, "kg/s"),
        ("mol", DPTMol, 14, 4, "mol"),
        ("momentum", DPTMomentum, 14, 53, "N/s"),
        ("percent", DPTScaling, 5, 1, "%"),
        ("percentU8", DPTPercentU8, 5, 4, "%"),
        ("percentV16", DPTPercentV16, 8, 10, "%"),
        ("percentV8", DPTPercentV8, 6, 1, "%"),
        ("phaseangledeg", DPTPhaseAngleDeg, 14, 55, "°"),
        ("phaseanglerad", DPTPhaseAngleRad, 14, 54, "rad"),
        ("power", DPTPower, 14, 56, "W"),
        ("power_2byte", DPTPower2Byte, 9, 24, "kW"),
        ("power_density", DPTPowerDensity, 9, 22, "W/m²"),
        ("powerfactor", DPTPowerFactor, 14, 57, None),
        ("ppm", DPTPartsPerMillion, 9, 8, "ppm"),
        ("pressure", DPTPressure, 14, 58, "Pa"),
        ("pressure_2byte", DPTPressure2Byte, 9, 6, "Pa"),
        ("prop_data_type", DPTPropDataType, 7, 10, None),
        ("pulse", DPTValue1Ucount, 5, 10, "counter pulses"),
        ("pulse_2byte", DPT2Ucount, 7, 1, "pulses"),
        ("pulse_2byte_signed", DPTValue2Count, 8, 1, "pulses"),
        ("pulse_4_ucount", DPTValue4Ucount, 12, 1, "counter pulses"),
        ("pulse_4byte", DPTValue4Count, 13, 1, "counter pulses"),
        ("rain_amount", DPTRainAmount, 9, 26, "L/m²"),
        ("reactance", DPTReactance, 14, 59, "Ω"),
        ("reactive_energy", DPTReactiveEnergy, 13, 12, "VARh"),
        ("reactive_energy_kvarh", DPTReactiveEnergykVARh, 13, 15, "kVARh"),
        ("resistance", DPTResistance, 14, 60, "Ω"),
        ("resistivity", DPTResistivity, 14, 61, "Ωm"),
        ("rotation_angle", DPTRotationAngle, 8, 11, "°"),
        ("scene_number", DPTSceneNumber, 17, 1, None),
        ("self_inductance", DPTSelfInductance, 14, 62, "H"),
        ("solid_angle", DPTSolidAngle, 14, 63, "sr"),
        ("sound_intensity", DPTSoundIntensity, 14, 64, "W/m²"),
        ("speed", DPTSpeed, 14, 65, "m/s"),
        ("stepwise_blinds", DPTControlStepwiseBlinds, 3, 8, "%"),
        ("stepwise_dimming", DPTControlStepwiseDimming, 3, 7, "%"),
        ("stress", DPTStress, 14, 66, "Pa"),
        ("string", DPTString, 16, 0, None),
        ("surface_tension", DPTSurfaceTension, 14, 67, "N/m"),
        ("tariff", DPTTariff, 5, 6, None),
        ("temperature", DPTTemperature, 9, 1, "°C"),
        ("temperature_a", DPTTemperatureA, 9, 3, "K/h"),
        ("temperature_difference", DPTTemperatureDifference, 14, 70, "K"),
        ("temperature_difference_2byte", DPTTemperatureDifference2Byte, 9, 2, "K"),
        ("temperature_f", DPTTemperatureF, 9, 27, "°F"),
        ("thermal_capacity", DPTThermalCapacity, 14, 71, "J/K"),
        ("thermal_conductivity", DPTThermalConductivity, 14, 72, "W/mK"),
        ("thermoelectric_power", DPTThermoelectricPower, 14, 73, "V/K"),
        ("time_1", DPTTime1, 9, 10, "s"),
        ("time_2", DPTTime2, 9, 11, "ms"),
        ("time_period_100msec", DPTTimePeriod100Msec, 7, 4, "ms"),
        ("time_period_10msec", DPTTimePeriod10Msec, 7, 3, "ms"),
        ("time_period_hrs", DPTTimePeriodHrs, 7, 7, "h"),
        ("time_period_min", DPTTimePeriodMin, 7, 6, "min"),
        ("time_period_msec", DPTTimePeriodMsec, 7, 2, "ms"),
        ("time_period_sec", DPTTimePeriodSec, 7, 5, "s"),
        ("time_seconds", DPTTimeSeconds, 14, 74, "s"),
        ("torque", DPTTorque, 14, 75, "Nm"),
        ("voltage", DPTVoltage, 9, 20, "mV"),
        ("volume", DPTVolume, 14, 76, "m³"),
        ("volume_flow", DPTVolumeFlow, 9, 25, "L/h"),
        ("volume_flux", DPTVolumeFlux, 14, 77, "m³/s"),
        ("volume_liquid_litre", DPTVolumeLiquidLitre, 12, 1200, "L"),
        ("volume_m3", DPTVolumeM3, 12, 1201, "m³"),
        ("weight", DPTWeight, 14, 78, "N"),
        ("wind_speed_kmh", DPTWspKmh, 9, 28, "km/h"),
        ("wind_speed_ms", DPTWsp, 9, 5, "m/s"),
        ("work", DPTWork, 14, 79, "J"),
    ],
)
def test_dpt_lookup(value_type, dpt_class, main, sub, unit):
    """Test DPT4ByteUnsigned."""
    dpt = DPTBase.parse_transcoder(value_type)
    assert dpt is dpt_class
    assert DPTBase.transcoder_by_dpt(dpt_main=main, dpt_sub=sub) is dpt_class
    assert dpt.unit == unit

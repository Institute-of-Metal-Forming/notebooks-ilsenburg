import numpy as np
from .flow_stress import FreibergFlowStressCoefficients
from scipy.optimize import fsolve

from .flow_stress import flow_stress
from .force_feb import testy_function_three, testy_function_four, testy_a


def beta(layer_thickness_1, layer_thickness_2):
    """Relationship between the layer thicknesses and therefore their influence"""
    return layer_thickness_1 / (layer_thickness_1 + layer_thickness_2)


def contact_length(
    height_at_start: float, height_end: float, roll_radius_current: float
):
    """Contact length with the roll with same lower and upper roll"""
    return np.sqrt(
        roll_radius_current * (height_at_start - height_end)
        - (((height_at_start - height_end) ** 2) / 4)
    )


def strain_phi(height_at_start: float, height_end: float):
    """strain of the material layer or overall work piece depending on the input, Umformgrad"""
    return np.log(height_at_start / height_end)


def strain_epsilon(height_at_start: float, height_end: float):
    """reduction of the material in numbers between 0 and 1"""
    return (height_at_start - height_end) / height_at_start


def equivalent_strain_rate(velocity: float, contact_arc: float, strain: float):
    """Equivalent strain rate according to Hoff and Dahl"""
    return velocity * strain / contact_arc


def flow_stress_diff(
    x: float,
    coefficients: FreibergFlowStressCoefficients,
    strain_rate: float,
    temperature: float,
    starting_height: float,
    flow_stress_second,
):
    """
    Calculates the flow stress according to the model from the provided coefficients, strain, strain rate and temperature.

    :param coefficients: the coefficients set to use
    :param x: height at the current coordinate
    :param strain_rate: the equivalent strain rate experienced
    :param temperature: the absolute temperature of the material (K)
    returns: the flow stress in Pa
    """

    strain = np.log(starting_height / x) + coefficients.baseStrain
    strain_rate = strain_rate + coefficients.baseStrainRate
    temperature = temperature - 273.15
    return (
        -(
            coefficients.a
            * np.exp(coefficients.m1 * temperature)
            * (strain**coefficients.m2)
            * (strain_rate**coefficients.m3)
            * np.exp(coefficients.m4 / strain)
            * ((1 + strain) ** (coefficients.m5 * temperature))
            * ((1 + strain) ** coefficients.m6)
            * np.exp(coefficients.m7 * strain)
            * (strain_rate ** (coefficients.m8 * temperature))
            * (temperature**coefficients.m9)
        )
    ) + flow_stress_second


def roll_force_feb(
    kf_m_clad, width_wp, roll_radius_current, height_at_start, height_end, factor_1
):
    delta_h = height_at_start - height_end
    return (
        1.15 * kf_m_clad * width_wp * np.sqrt(roll_radius_current * delta_h) * factor_1
    )


def roll_torque_feb(
    roll_radius_current, height_at_start, height_end, kf_m_clad, width_wp, factor_2
):
    return (
        2
        * roll_radius_current
        * (height_at_start**2)
        * kf_m_clad
        * width_wp
        * factor_2
        / height_end
    )


def roll_force_and_torque(
    radius,
    upper_material_coeff,
    lower_material_coeff,
    height_layer_upper: float,
    height_layer_lower: float,
    temperature: float,
    width: float,
    roll_velocity: float,
    friction_coefficient: float,
    roll_gap: float,
):
    height_start = height_layer_upper + height_layer_lower
    contact_arc = contact_length(height_start, roll_gap, radius)
    strain_overall = strain_phi(height_start, roll_gap)
    strain_rate_equivalent = equivalent_strain_rate(
        roll_velocity, contact_arc, strain_overall
    )
    flow_stress_upper = flow_stress(
        0, upper_material_coeff, strain_rate_equivalent, temperature
    )
    flow_stress_lower = flow_stress(
        0, lower_material_coeff, strain_rate_equivalent, temperature
    )
    # Sort
    if flow_stress_upper > flow_stress_lower:
        flow_stress_harder = flow_stress_upper
        flow_stress_softer = flow_stress_lower
        coeff_soft = lower_material_coeff
        coeff_hard = upper_material_coeff
        start_height_soft = height_layer_lower
        start_height_hard = height_layer_upper
    else:
        flow_stress_harder = flow_stress_lower
        flow_stress_softer = flow_stress_upper
        coeff_soft = upper_material_coeff
        coeff_hard = lower_material_coeff
        start_height_soft = height_layer_upper
        start_height_hard = height_layer_lower
    # Calculate bonding point and height
    height_bonding = fsolve(
        flow_stress_diff,
        x0=np.array([0.0019]),
        args=(
            coeff_soft,
            strain_rate_equivalent,
            temperature,
            start_height_soft,
            flow_stress_harder,
        ),
    )[0]
    layer_relationship = beta(height_bonding, start_height_hard)
    end_height_soft = layer_relationship * roll_gap
    end_height_hard = (1 - layer_relationship) * roll_gap
    # Calculating mean flow stress
    end_strain_soft = strain_phi(
        height_at_start=start_height_soft, height_end=end_height_soft
    )
    end_strain_hard = strain_phi(
        height_at_start=start_height_hard, height_end=end_height_hard
    )
    end_flow_stress_soft = flow_stress(
        end_strain_soft, coeff_soft, strain_rate_equivalent, temperature
    )
    end_flow_stress_hard = flow_stress(
        end_strain_hard, coeff_hard, strain_rate_equivalent, temperature
    )
    weight = 2  # geometrical vs. analytical weighting can be changed here (1 vs 2)
    mean_flow_stress = (
        flow_stress_softer
        + weight * end_flow_stress_soft
        + flow_stress_harder
        + weight * end_flow_stress_hard
    ) / (4 + (weight - 1) * 2)
    # Calculate the roll force and torque according to FEB
    height_start = start_height_soft + start_height_hard
    strain_overall = strain_phi(height_start, roll_gap)
    a = testy_a(friction_coefficient, radius, roll_gap)
    r = strain_epsilon(height_start, roll_gap)
    f1 = testy_function_three(a, r)
    f2 = testy_function_four(a, r)
    roll_force = roll_force_feb(
        mean_flow_stress, width, radius, height_start, roll_gap, f1
    )
    roll_torque = roll_torque_feb(
        radius, height_start, roll_gap, mean_flow_stress, width, f2
    )
    return roll_force, roll_torque

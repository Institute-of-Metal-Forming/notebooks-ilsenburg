import numpy as np
import scipy.integrate as integrate

def testy_a(friction_coeff: float, radius:float, height_end: float):
    """Dimensionless coefficient of FEB, Equation (41)"""
    return friction_coeff * np.sqrt(radius / height_end)

def testy_r(height_at_start: float, height_end: float):
    """reduction of the material in numbers between 0 and 1, (FEB, Equation (42))"""
    return (height_at_start - height_end) / height_at_start

def testy_uppercase_phi_entry(coeff_a, reduction):
    """Relationship: angle at entry / friction coefficient, FEB, Equation (46)"""
    return (1 / coeff_a) * np.sqrt(reduction / (1 - reduction))

def testy_uppercase_phi_neutral_point(coeff_a, reduction):
    """Relationship: angle at the neutral point / friction coefficient, FEB, Equation (46)"""
    return (1 / coeff_a) * (np.tan(0.5 * np.arctan(np.sqrt(reduction / (1 - reduction)))
                                   - ((1 / (4 * coeff_a)) * np.log(1 / (1 - reduction)))))

def testy_function_three(coeff_a, reduction):
    """Force function according to FEB, Equation (55)"""
    def testy_function_one():
        """Part of the Force function according to FEB, Equation (51)"""
        def core_equation(x, switch=1):
            return (1 + (coeff_a ** 2) * (x ** 2)) * np.exp(switch * 2 * coeff_a * np.arctan(coeff_a * x))
        first_part_result = integrate.quad(lambda x: core_equation(x), 0, testy_uppercase_phi_neutral_point(coeff_a, reduction))
        second_part_result = integrate.quad(lambda x: core_equation(x, -1), testy_uppercase_phi_neutral_point(coeff_a, reduction), testy_uppercase_phi_entry(coeff_a, reduction))
        return first_part_result[0] + (1 - reduction) * np.exp(2 * coeff_a * np.arctan(np.sqrt(reduction / (1 - reduction)))) * second_part_result[0]
    return coeff_a * np.sqrt((1 - reduction) / reduction) * testy_function_one()

def testy_function_four(coeff_a, reduction):
    """Torque function according to FEB, Equation (56)"""
    def testy_function_two():
        """Part of the Torque function according to FEB, Equation (54)"""
        def core_equation(x, switch=1):
            return (1 + (coeff_a ** 2) * (x ** 2)) * np.exp(switch * 2 * coeff_a * np.arctan(coeff_a * x)) * x
        first_part_result = integrate.quad(lambda x: core_equation(x), 0, testy_uppercase_phi_neutral_point(coeff_a, reduction))
        second_part_result = integrate.quad(lambda x: core_equation(x, -1), testy_uppercase_phi_neutral_point(coeff_a, reduction), testy_uppercase_phi_entry(coeff_a, reduction))
        return first_part_result[0] + (1 - reduction) * np.exp(2 * coeff_a * np.arctan(np.sqrt(reduction / (1 - reduction)))) * second_part_result[0]
    return (coeff_a ** 2) * ((1 - reduction) ** 2) * testy_function_two()
from flow_stress import FreibergFlowStressCoefficients

koeff_ni_cold = FreibergFlowStressCoefficients(
    a=752 * 1e6,
    m1=-0.000656,
    m2=0.22981,
    m3=-0.00311,
    m4=-0.00124,
    m5=0,
    m6=0,
    m7=0,
    m8=0,
    m9=0,
)

koeff_ti_warm = FreibergFlowStressCoefficients(
    a=3518.6 * 1e6,
    m1=-0.00327,
    m2=0.68022,
    m3=0,
    m4=0.03841,
    m5=-0.00121,
    m6=0,
    m7=-0.43501,
    m8=0.000186,
    m9=0,
)

koeff_almg25_cold_v1 = FreibergFlowStressCoefficients(
    a=153.939, m1=-0.00182, m2=0.22160, m3=0.02950, m4=0.00210
)

koeff_almg25_cold_v2 = FreibergFlowStressCoefficients(
    a=179.756, m1=-0.00283, m2=0.18870, m3=0.04334, m4=-0.00571
)

koeff_almg15_cold = FreibergFlowStressCoefficients(
    a=217.519, m1=-0.00096, m2=0.15361, m3=0.01201, m4=0.00040
)

koeff_almg3_v1_cold = FreibergFlowStressCoefficients(
    a=270.102, m1=-0.00098, m2=0.11837, m3=-0.00533, m4=-0.00380
)

koeff_trip = FreibergFlowStressCoefficients(
    a=0.755002 * 1e6,
    m1=-0.00359875,
    m2=0.394698,
    m3=0.0346997,
    m4=0.00036809,
    m5=-0.0000689626,
    m6=0,
    m7=-0.365104,
    m8=-0.00000345044,
    m9=1.39308,
)

koeff_twip = FreibergFlowStressCoefficients(
    a=1.17058 * 1e6,
    m1=-0.00326796,
    m2=0.392316,
    m3=-0.0185245,
    m4=0.00130981,
    m5=-0.0000956118,
    m6=0,
    m7=-0.371706,
    m8=0.000058272,
    m9=1.27846,
)

"""
Core mathematical engine for Zeta factor calculation.
"""

import math
from .standards import standards

# ============================================
# ZETA CALIBRATION AND STANDARD DEVIATION σ(ζ)
# ============================================

def calc_zeta(std, mineral, lambda_a, lambda_a_err, g, N_D, N_S, N_I, rho_S, rho_I, rho_D):
    """Calculate Zeta factor and its uncertainty.

    Parameters:
    N_S : int
        Number of spontaneous tracks.
    N_I : int
        Number of induced tracks.
    N_D : int
        Number of dosimeter tracks.
    rho_S : float
        Spontaneous track density [cm^-2].
    rho_I : float
        Induced track density [cm^-2].
    rho_D : float
        Dosimeter track density (if used).
    std : tuple
        Standard parameters: (name, age [Ma], uncertainty [Ma], Ap, Zrn, Ttn).

    Returns:
    zeta_user : float
        Calculated Zeta factor using user equation.
    sigma_zeta : float
        Uncertainty of the Zeta factor.
    rel_sigma_percent : float
        Relative uncertainty of the Zeta factor [%].
    """

    # --- EXTRACT STANDARD PARAMETERS ---
    #print(f"Mineral: {mineral}, type: {type(mineral)}")
    #print(f"Standard: {std}, type: {type(std)}")

    t_sm = standards[std][1]      # Known age of standard [Ma]
    sig_T = standards[std][2]     # Uncertainty of standard age [Ma]

    #print(f"Standard age: {t_sm} Ma ± {sig_T} Ma")
    #print(f"Lambda_a: {lambda_a} yr^-1 ± {lambda_a_err} yr^-1")

    # --- CONVERSION TO YEARS ---
    t_sm_yr = t_sm * 1e6

    # --- EQUATION ---
    zeta_user = (math.exp(lambda_a * t_sm_yr) - 1) / (lambda_a * (rho_S / rho_I) * g * rho_D)

    # UNCERTAINTY OF ζ
    sig_zeta = zeta_user * math.sqrt(
        (1 / N_S) +
        (1 / N_I) +
        (1 / N_D) +
        math.pow((sig_T / t_sm), 2)
    )

    rel_sig = 100 * sig_zeta / zeta_user

    zeta_user = zeta_user / 1e6  # Convert to Ma/cm^2
    sig_zeta = sig_zeta / 1e6    # Convert to Ma/cm^2
    
    return {"zeta_user": zeta_user,
            "sigma_zeta": sig_zeta,
            "rel_sigma_percent": rel_sig}


if __name__ == "__main__":
    pass
    # # ===================================================
    # # ZETA CALIBRATION AND STANDARD DEVIATION σ(ζ) - TEST
    # # ===================================================

    # # --- SETTING PARAMETERS ---
    # # --- Decay onstant and error
    # lambda_a = 1.55125e-10     # Decay constant of 238U [yr^-1]
    # sig_lambda_a = 0.00333e-10 # Error in the decay constant of 238U [yr^-1]

    # # Durango (McDowell et al. 2005)
    # std = "DUR"    # Standard
    # mineral = "Ap" # Mineral
    # t_sm = 31.44              # Known age of Durango standard [Ma]
    # sig_T = 0.018             # Durango standard age error [Ma]

    # # Setting the relevant parameters for fission track counting
    # rho_S = 210321.91         # Density od spontaneous fission tracks [cm^-2]
    # rho_I = 536061.05         # Density of induced fission tracks [cm^-2]
    # rho_D = 0.66973           # Density of fission tracks on the U-glass dosimeter (if used)
    # g = 0.5                   # Geometric factor (0.5 = External detector method)
    # N_S = 769                 # Number of spontaneous fission tracks
    # N_I = 1960                # Number of induced fission tracks
    # N_D = 5881                # Number of fission tracks on the U-glass dosimeter

    # # Calling the calc_zeta function
    # result = calc_zeta(std, mineral, lambda_a, lambda_a_err, g, N_D, N_S, N_I, rho_S, rho_I, rho_D)

    # #print(result)
    # print("-" * 80)
    # print(f"Standard used: {standards[std][0]}, {standards[std][1]} ± {standards[std][2]} Ma")
    # print(f"Zeta (user equation): {result['zeta_user']:.2f} Ma.cm\u00B2")
    # print(f"Uncertainty of Zeta: {result['sigma_zeta']:.2f} Ma.cm\u00B2") 
    # print(f"Relative uncertainty: {result['rel_sigma_percent']:.2f} %")
    # print("-" * 80)

# End of Script (c) Rasto Vojtko

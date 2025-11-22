#!/usr/bin/env python3

"""Function for calculation of Zeta factor for Fission track analysis.

Copyright (C) 2025 Rasto Vojtko

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import math


# Default constants for Zeta calculations
lambda_a = 1.55125e-10     # decay constant of 238U [yr^-1]
lambda_a_err = 0.00333e-10 # uncertainty of decay constant of 238U [yr^-1]
g = 0.5                    # geometric factor (0.5 = external detector)


# GEOCHRONOLOGY STANDARDS
""" Geochronoly standards: abreviation -> (name, age, uncertainty, Ap, Zrn, Ttn)
Note: True, False for Ap, Zrn, Ttn

APATITE STANDARDS:
Durango (DUR): 
McDowell, F.W., McIntosh, W.C., and Farley, K.A., 2005. A precise 
40Ar-39Ar reference age for the Durango apatite (U-Th)/He and fission 
track dating standard. Chemical Geology, 214, 249-263.

Duluth Complex (FC1):
Paces, J.B. and Miller, J.D., 1993. Precise UPb ages of Duluth Complex 
and related mafic intrusions, northeastern Minnesota: Geochronological 
insights to physical, petrogenic, paleomagnetic, and tectonomagmatic 
processes associated with the 1.1 Ga Midcontinent Rift System. 
Journal of Geophysical Research, 98, B8, 13997-14013.

Fish Canyon Tuff (FCT):
Kuiper, K.F., Deino, A., Hilgen, P.J., Krijgsman, W., Renne, P.R., 
and Wijbrans, J.R., 2008. Synchronizing rock clocks of Earth history. 
Science, 320, 500-504.
Lanphere, M.A. and Baadsraard, H., 2001. Precise K-Ar, 40 Ar/39 Ar,
Rb-Sr and U-Pb mineral ages from the 27.5 Ma Fish Canyon Tuff 
reference standard. Chemical Geology, 175, 653-671.

Mount Dromedary (MD):
Renne, P.R., Swisher, C.C., Deino, A.L., Karner, D.B., Owens, T.L., 
and DePaolo, D.J., 1998. Intercalibration of standards, absolute 
ages and uncertainties in 40 Ar/39 Ar dating. Chemical Geology, 
45, 117-152.

Mount McClure (MM):
Schoene, B., and Bowring, S.A., 2006. U–Pb systematics of the McClure 
Mountain syenite: thermochronological constraints on the age of the 
40Ar/39Ar standard MMhb. Contributions to Mineralogy and Petrology, 
151, 615-630.

Tardree Rhyolite (TR):
Ganerød, M., Chew, D.M., Smethurst, M.A., Troll, V.R., Corfu, F., 
Meade,F., Prestvik, T., 2011. Geochronology of the Tardree Rhyolite 
Complex, Northern Ireland: Implications for zircon fission track 
studies, the North Atlantic Igneous Province and the age of the Fish 
Canyon sanidine standard. Chemical Geology, 286, 3-4, 222-228.

TEMORA2 - Middledale gabbroic diorite (TEM2):
lack, L.P., Kamo, S.L., Allen, C.M., Davis, D.W., Aleinikoff, J.N., 
Valley, J.W., Mundil, R., Campbell, I.H., Korsch, R.J., Williams, 
I.S., and Foudoulis, C. 2004. Improved 206 Pb/238 U microprobe 
geochronology by the monitoring of trace-element-related matrix effect; 
SHRIMP, ID-TIMS, ELA-ICP-MS and oxygen isotope documentation for a series 
of zircon standards. Chemical Geology, 205, 15-140

Note: Check TEM2 for other minerals!
"""
minerals = {
    "Ap": "Apatite",
    "Zrn": "Zircon",
    "Ttn": "Titanite",
}

standards = {
    "FCT": ["Fish Canyon Tuff", 28.201, 0.012, True, True, True],
    "FC1": ["Duluth Complex", 1099.0, 0.6, True, True, False],
    "DUR": ["Durango", 31.44, 0.018, True, False, False],
    "MD": ["Mount Dromedary", 99.12, 0.14, True, True, False],
    "MM": ["Mount McClure", 523.51, 1.47, True, True, True],
    "TEM2": ["TEMORA2", 416.78, 0.33, False, True, False],
    "TR": ["Tardree Rhyolite", 61.23, 0.11, False, True, False],
}

# ========================================
# ZETA KALIBRÁCIA A CHYBA σ(ζ)
# ========================================

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
    zeta_HG : float
        Calculated Zeta factor using Hurford & Green (1983) equation.
    t_calc_Ma : float
        Recalculated age from Zeta factor [Ma].
    sig_zeta : float
        Uncertainty of the Zeta factor.
    rel_sig : float
        Relative uncertainty of the Zeta factor [%].
    """

    # --- EXTRACT STANDARD PARAMETERS ---
    print(f"Mineral: {mineral}, type: {type(mineral)}")
    print(f"Standard: {std}, type: {type(std)}")

    t_sm = standards[std][1]      # known age of standard [Ma]
    sig_T = standards[std][2]     # uncertainty of standard age [Ma]

    print(f"Standard age: {t_sm} Ma ± {sig_T} Ma")
    print(f"Lambda_a: {lambda_a} yr^-1 ± {lambda_a_err} yr^-1")

    # # --- PREPOČET NA ROKY ---
    t_sm_yr = t_sm * 1e6

    # 1) User equation:
    zeta_user = (math.exp(lambda_a * t_sm_yr) - 1) / (lambda_a * (rho_S / rho_I) * g * rho_D)

    # # 2) Hurford & Green (1983)
    # zeta_HG = (lambda_a * g * rho_S) / (rho_I * (math.exp(lambda_a * t_sm_yr) - 1))

    # # 3) Recalculate age from ζ_HG
    # t_calc_yr = (1 / lambda_a) * math.log(1 + (lambda_a * g * rho_S) / (zeta_HG * rho_I))
    # t_calc_Ma = t_calc_yr / 1e6

    # 4) Uncertainty of ζ
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
    # # Example usage
    # N_S = 391  # Number of spontaneous tracks
    # N_I = 1027  # Number of induced tracks
    # N_D = 5881  # Number of dosimeter tracks
    # rho_S = 0.1938e6  # Spontaneous track density [cm^-2]
    # rho_I = 0.5090e6  # Induced track density [cm^-2]
    # rho_D = 0.669727e6  # Dosimeter track density [cm^-2]
    std = "DUR"    # Standard
    mineral = "Ap" # Mineral


    # --- ZADANIE PARAMETROV ---
    lambda_a = 1.55125e-10     # rozpadová konštanta 238U [yr^-1]
    sig_lambda_a = 0.00333e-10 # chyba veku rozpadovej konštanty 238U [yr^-1]

    # Durango (McDowell et al. 2005)
    t_sm = 31.44              # známy vek štandardu [Ma]
    sig_T = 0.018             # chyba veku štandardu [Ma]
    rho_S = 210321.91         # spontánne stopy [cm^-2]
    rho_I = 536061.05         # indukované stopy [cm^-2]
    rho_D = 0.66973           # dosimeter (ak sa používa)
    g = 0.5                   # geometrický faktor (0.5 = externý detektor)
    N_S = 769                 # počet spontánnych stôp
    N_I = 1960                # počet indukovaných stôp
    N_D = 5881                # počet stôp na dosimetri U-sklíčka

    # zeta_user, zeta_HG, t_calc_Ma, sig_zeta, rel_sig = calc_zeta(std, mineral, lambda_a, lambda_a_err, g, N_D, N_S, N_I, rho_S, rho_I, rho_D 
    # )

    zeta_user, zeta_HG, t_calc_Ma, sig_zeta, rel_sig = calc_zeta(
        std, mineral, lambda_a, lambda_a_err, g, N_D, N_S, N_I, rho_S, rho_I, rho_D 
    )

    print(f"Zeta (user equation): {zeta_user:.4e}")
    print(f"Zeta (Hurford & Green): {zeta_HG:.4e}")
    print(f"Recalculated age: {t_calc_Ma:.2f} Ma")
    print(f"Uncertainty of Zeta: {sig_zeta:.4e}")
    print(f"Relative uncertainty: {rel_sig:.2f} %")
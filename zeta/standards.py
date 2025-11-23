
# --- DEFAULT CONSTANTS FOR ZETA CALCULATIONS ---
lambda_a = 1.55125e-10     # Decay constant of 238U [yr^-1]
lambda_a_err = 0.00333e-10 # Uncertainty of decay constant of 238U [yr^-1]
g = 0.5                    # Geometric factor (0.5 = external detector method)


# --- GEOCHRONOLOGY STANDARDS ---
""" Geochronogy standards: abreviation -> (name, age, uncertainty, Ap, Zrn, Ttn)
Note: True, False for Ap, Zrn, Ttn

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

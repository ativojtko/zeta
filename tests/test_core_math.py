# tests/test_core_math.py

import pytest
from zeta.core import calc_zeta # Importujeme funkciu, ktorú chceme testovať
from zeta.standards import LAMBDA_A, LAMBDA_A_ERR, G 

# Dáta pre Durango (DUR), kde poznáme výsledok
DURANGO_INPUTS = {
    "std": "DUR",
    "mineral": "Ap",
    "lambda_a": LAMBDA_A,
    "lambda_a_err": LAMBDA_A_ERR,
    "g": G,
    "N_D": 5881,
    "N_S": 769,
    "N_I": 1960,
    "rho_S": 210321.91,
    "rho_I": 536061.05,
    "rho_D": 0.66973,
}

# Očakávané výsledky z vášho predchádzajúceho testu (239.88 a 10.68)
EXPECTED_ZETA = 239.88
EXPECTED_SIGMA = 10.68

def test_zeta_durango_calculation():
    """Testuje, či calc_zeta vráti správne známe hodnoty pre Durango."""
    
    # Spustenie kalkulácie s testovacími vstupmi (používame ** na rozbalenie slovníka)
    result = calc_zeta(**DURANGO_INPUTS)
    
    # Overenie výsledkov
    
    # 1. Overenie Zety (použijeme 'assert' a zaokrúhlenie na 2 desatinné miesta)
    # math.isclose() je lepší, ale pre jednoduchosť použijeme assert round()
    assert round(result['zeta_user'], 2) == EXPECTED_ZETA
    
    # 2. Overenie Sigma (neistoty)
    assert round(result['sigma_zeta'], 2) == EXPECTED_SIGMA
    
    # 3. Overenie, že relatívna chyba je > 0 (základný sanity check)
    assert result['rel_sigma_percent'] > 0
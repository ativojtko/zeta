"""
Zeta Factor Calculation Tool for Fission-Track Dating.

Provides the core mathematical engine for calculating the Zeta factor.
"""

# Importovanie verzie
from .version import APP_VERSION as __version__

# Exponovanie kľúčových funkcií z 'core'
# Toto umožní použiť 'from zeta import calc_zeta'
from .core import calc_zeta
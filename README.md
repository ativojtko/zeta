# Zeta Factor Calculator (zeta-factor)

## 🔭 Prehľad

`zeta-factor` je nástroj príkazového riadku (CLI) pre rýchly a presný výpočet faktora Zeta ($\zeta$) pre datovanie metódou stôp štiepenia (fission-track dating). Aplikácia je vyvinutá v Pythone a používa štandardné geochronologické referenčné dáta.

---

## 🚀 Inštalácia

### Používatelia

Nástroj je možné nainštalovať priamo z PyPI (po publikovaní):

```bash
pip install zeta-factor
Vývojári
Pre vývoj a testovanie (ak si chcete upravovať kód), použite inštaláciu v editovateľnom režime (editable mode):

Bash

# Uistite sa, že ste v koreňovom adresári Zeta/
pip install -e .
🛠️ Použitie
Po inštalácii je príkaz dostupný ako zeta.

Zobrazenie verzie a pomoci
Pre rýchlu kontrolu verzie alebo zobrazenie všetkých povinných argumentov:

Bash

# Zobrazenie verzie
zeta --version

# Zobrazenie pomoci a parametrov
zeta --help
Príklad výpočtu
Nástroj vyžaduje zadanie štandardu, minerálu a kľúčových počtov/hustôt stôp.

Príklad (Durango Apatite):

Bash

zeta --std DUR --mineral Ap \
     --Ns 769 --Ni 1960 --Nd 5881 \
     --rhoS 210321.91 --rhoI 536061.05 --rhoD 0.66973
🧪 Testovanie
Projekt používa pytest na zabezpečenie správnosti matematického jadra. Pre spustenie testov v lokálnom prostredí (v adresári Zeta/):

Bash

# Nainštalujte si pytest, ak ho ešte nemáte
pip install pytest

# Spustite testy
pytest
📚 Štandardy a Referencie
Referenčné dáta (veky štandardov, konštanty) sú uložené v súbore zeta/standards.py. Presné veky a ich neistoty vychádzajú z nasledujúcich publikácií:

Durango (DUR): McDowell, F.W., McIntosh, W.C., and Farley, K.A., 2005. A precise 40Ar-39Ar reference age for the Durango apatite... Chemical Geology, 214, 249-263.

Duluth Complex (FC1): Paces, J.B. and Miller, J.D., 1993. Precise UPb ages of Duluth Complex... Journal of Geophysical Research, 98, B8, 13997-14013.

Fish Canyon Tuff (FCT): Kuiper, K.F. et al., 2008. Synchronizing rock clocks of Earth history. Science, 320, 500-504. A Lanphere, M.A. and Baadsraard, H., 2001. Precise K-Ar, 40Ar/39Ar, Rb-Sr and U-Pb mineral ages... Chemical Geology, 175, 653-671.

Mount Dromedary (MD): Renne, P.R. et al., 1998. Intercalibration of standards... Chemical Geology, 45, 117-152.

Mount McClure (MM): Schoene, B., and Bowring, S.A., 2006. U–Pb systematics of the McClure Mountain syenite... Contributions to Mineralogy and Petrology, 151, 615-630.

Tardree Rhyolite (TR): Ganerød, M. et al., 2011. Geochronology of the Tardree Rhyolite Complex... Chemical Geology, 286, 3-4, 222-228.

TEMORA2 (TEM2): Black, L.P. et al., 2004. Improved 206Pb/238U microprobe geochronology... Chemical Geology, 205, 15-140.

⚖️ Licencia
Tento projekt je licencovaný pod Licenciou MIT. Podrobnosti nájdete v súbore LICENSE.

Copyright (c) 2025 Rastislav Vojtko
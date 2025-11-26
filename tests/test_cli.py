# tests/test_cli.py

import sys
import pytest
from zeta.cli.cli import run_cli # Importujeme funkciu pre spustenie CLI
from zeta.version import APP_VERSION

# Umožňuje zachytiť výstup konzoly (print)
def test_cli_version_check(capsys, monkeypatch):
    """Testuje, či príkaz '--version' správne vypíše verziu a ukončí aplikáciu."""
    
    # Použitie monkeypatch na nastavenie sys.argv (simulujeme zadanie príkazu)
    monkeypatch.setattr(sys, 'argv', ['zeta', '--version'])
    
    # Očakávame, že run_cli() skončí s ukončením (exit code 0), pretože --version má sys.exit(0)
    with pytest.raises(SystemExit) as e:
        run_cli()
        
    # Kontrola, či bol ukončovací kód 0
    assert e.value.code == 0
    
    # Kontrola výstupu do konzoly (stdout)
    captured = capsys.readouterr()
    expected_output = f"Zeta CLI version {APP_VERSION}\n"
    
    assert captured.out == expected_output
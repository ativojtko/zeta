#!/usr/bin/env python3

import sys
import argparse
from zeta import APP_VERSION

def run_cli():
    #print("RUN CLI")
    #------------------------------------------------------------
    # PRE-PARSER (rieši --version pred hlavnými „required“ args)
    # ------------------------------------------------------------
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--version", action="store_true")

    # Pre-parser spracuje len --version a nič viac
    pre_args, remaining_argv = pre_parser.parse_known_args()

    # Funguje SAMOSTATNE:
    if pre_args.version:
        print(f"Zeta CLI version {APP_VERSION}")
        sys.exit(0)


if __name__ == "__main__":
    run_cli()
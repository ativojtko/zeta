#!/usr/bin/env python3

import sys
import argparse
from zeta import calc_zeta, standards, minerals, lambda_a, lambda_a_err, g, APP_VERSION

def run_cli():
    #------------------------------------------------------------
    # PRE-PARSER (handles --version before the main "required" args)
    # ------------------------------------------------------------
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument("--version", action="store_true", help="Program version")

    # The pre-parser only processes --version and nothing else.
    pre_args, remaining_argv = pre_parser.parse_known_args()

    # Works Independently:
    if pre_args.version:
        print(f"Zeta CLI version {APP_VERSION}")
        sys.exit(0)

    # ------------------------------------------------------------
    # MAIN PARSER – required arguments are here
    # ------------------------------------------------------------
    parser = argparse.ArgumentParser(
        prog="zeta-cli.py",
        description="Command-line Zeta factor calculator for fission-track dating.",
        epilog="Example:\n"
               "  zeta-cli.py --std DUR --mineral Ap "
               "--Ns 769 --Ni 1960 --Nd 5881 "
               "--rhoS 210321.91 --rhoI 536061.05 --rhoD 0.66973",
        formatter_class=argparse.RawTextHelpFormatter,
        parents=[pre_parser]   # <- important
    )

    # Required scientific parameters
    parser.add_argument("--std", type=str, required=True,
                        help=f"Standard code ({', '.join(standards.keys())})")
    parser.add_argument("--mineral", type=str, required=True,
                        help=f"Mineral code ({', '.join(minerals.keys())})")

    parser.add_argument("--Ns", type=int, required=True, help="Number of spontaneous tracks")
    parser.add_argument("--Ni", type=int, required=True, help="Number of induced tracks")
    parser.add_argument("--Nd", type=int, required=True, help="Number of dosimeter tracks")

    parser.add_argument("--rhoS", type=float, required=True, help="Spontaneous track density [cm^-2]")
    parser.add_argument("--rhoI", type=float, required=True, help="Induced track density [cm^-2]")
    parser.add_argument("--rhoD", type=float, required=True, help="Dosimeter track density [cm^-2]")

    # Optional override constants
    parser.add_argument("--lambdaA", type=float, default=lambda_a)
    parser.add_argument("--lambdaA_err", type=float, default=lambda_a_err)
    parser.add_argument("--g", type=float, default=g)

    args = parser.parse_args(remaining_argv)

    print(args)


if __name__ == "__main__":
    run_cli()
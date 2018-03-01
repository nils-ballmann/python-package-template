#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-03-01 14:18:34'

import argparse as ap
import sys


from . import __version__
from . import helper as h


def parse_args(args):
    if args is None:
        args = sys.argv[1:]

    parser = ap.ArgumentParser(prog='PACKAGE_NAME', add_help=False)

    parser.add_argument('-h', '--help', action='help', default=ap.SUPPRESS, help='Show this help message and exit.')
    parser.add_argument(
        '-V',
        '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__),
        help='Show version and exit.'
    )
    parser.add_argument(
        '-v', '--verbose', default=0, action='count', help='Increase output verbosity (use up to three times).'
    )

    args = parser.parse_args(args)
    return args


def main(args=None):
    args = parse_args(args)

    if args.verbose > 0:
        h.print_line()
        print('PACKAGE_NAME {}'.format(__version__))
        h.print_line()
        print('py: {}'.format(sys.version))
        h.print_line()
    if args.verbose > 1:
        print(repr(args))
        h.print_line()

    PACKAGE_MAIN

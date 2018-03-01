#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-03-01 14:51:44'

__version_info__ = [PACKAGE_MAJOR_VERSION, PACKAGE_MINOR_VERSION, PACKAGE_PATCH_VERSION]
__version__ = '.'.join([str(digit) for digit in __version_info__])

from .main import main

PACKAGE_PUBLIC_API

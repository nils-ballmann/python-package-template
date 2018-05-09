#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-04-13 11:04:46'

__version_info__ = [PACKAGE_MAJOR_VERSION, PACKAGE_MINOR_VERSION, PACKAGE_PATCH_VERSION]
__version__ = '.'.join([str(digit) for digit in __version_info__])

__all__ = [
    'PACKAGE_PUBLIC_API'
]

from .tool import main

PACKAGE_PUBLIC_API

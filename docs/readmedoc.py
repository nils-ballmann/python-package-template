#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111
"""
    A sphinx extension that pulls up package READMEs for inclusion in documentation.

    READMEs in formats other than rst will be converted using pandoc.
"""

import os
import pathlib as pl
import shutil as sh

from sphinx.util import logging

__updated__ = '2018-04-13 10:39:08'

__version_info__ = [1, 0, 0]
__version__ = '.'.join([str(digit) for digit in __version_info__])

LOGGER = logging.getLogger(__name__)

BUILDER_ATTRIBUTE = '_readmedoc_temp'


def pull_readme(app):
    doc_readmes = list(pl.Path(app.srcdir).glob('README.*'))
    if doc_readmes:
        LOGGER.warning('Docs source directory already contains a README, package README will not be pulled up.')
        return

    package_readmes = list(pl.Path(app.srcdir).parent.glob('README.*'))
    if not package_readmes:
        LOGGER.warning('No README found in package.')
        return
    elif len(package_readmes) > 1:
        LOGGER.warning('More than one README found in package. None will be included in the docs.')
        return

    readme = package_readmes.pop()
    if readme.suffix == '.rst':
        LOGGER.info('README already of type .rst, copying.')
        sh.copy(readme, app.srcdir)
        return

    try:
        import pypandoc
        output = pypandoc.convert_file(str(readme), to='rst')
        output = output.replace('\r\n', '\n')
        target = pl.Path(app.srcdir) / 'README.rst'
        with open(target, 'w') as target_file:
            target_file.write(output)
        if not hasattr(app.builder, BUILDER_ATTRIBUTE):
            setattr(app.builder, BUILDER_ATTRIBUTE, target)
    except ImportError:
        print('Package \'pypandoc\' not found. README will not be included.')
    except OSError:
        print('Binaries \'pandoc\' not found. README will not be included.')


def cleanup(app, exc):
    if hasattr(app.builder, BUILDER_ATTRIBUTE):
        tempfile = getattr(app.builder, BUILDER_ATTRIBUTE)
        if isinstance(tempfile, pl.Path) and tempfile.is_file and tempfile.parent == pl.Path(app.srcdir):
            try:
                os.remove(str(tempfile))
            except OSError:
                LOGGER.warning('Could not delete temporary README.')


def setup(app):
    app.connect('builder-inited', pull_readme)
    app.connect('build-finished', cleanup)
    return {'version': __version__}

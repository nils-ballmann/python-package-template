#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-03-01 14:42:06'

from setuptools import find_packages, setup

import PACKAGE_NAME


def readme():
    try:
        import pypandoc
        output = pypandoc.convert_file('README.md', to='rst', format='md')
        output = output.replace('\r\n', '\n')
        return output
    except ImportError:
        print('Package \'pypandoc\' not found. Using raw \'README.md\'.')
    except OSError:
        print('Binaries \'pandoc\' not found. Using raw \'README.md\'.')

    with open('README.md') as readme_file:
        return readme_file.read()


def requirements():
    with open('requirements.txt') as req_file:
        return list(map(lambda s: s.strip(), req_file.readlines()))


# https://pypi.python.org/pypi?%3Aaction=list_classifiers

setup(
    author='PACKAGE_AUTHOR',
    author_email='PACKAGE_AUTHOR_MAIL',
    classifiers=[
        'Development Status :: 3 - Alpha', 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6', 'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux', 'Natural Language :: English'
    ],
    description='PACKAGE_SHORT_DESCRIPTION',
    entry_points={
        'console_scripts': ['PACKAGE_EXECUTABLE=PACKAGE_NAME.main:main'],
    },
    include_package_data=True,
    install_requires=requirements(),
    license='MIT',
    long_description=readme(),
    name='PACKAGE_NAME',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.6, <4',
    test_suite='nose.collector',
    tests_require=['nose', 'coverage'],
    url='PACKAGE_URL',
    version=PACKAGE_NAME.__version__,
    zip_safe=False
)

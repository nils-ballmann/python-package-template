#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# pylint: disable=C0111

__updated__ = '2018-03-01 14:14:34'

import itertools as it
import xml.dom.minidom as m
import xml.etree.ElementTree as et


def grouper(iterable, chunk_size, fillvalue=None):
    '''
    Collect data into fixed-length chunks or blocks

    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    '''
    args = [iter(iterable)] * chunk_size
    return it.zip_longest(*args, fillvalue=fillvalue)


def repr_hex(value):
    if not isinstance(value, (bytes, bytearray)):
        raise TypeError('"value" must be of type "bytes" or "bytearray"')
    return 'b\'{}\''.format(
        ''.join('\\x{}'.format(''.join(byte_tuple).upper()) for byte_tuple in grouper(value.hex(), 2))
    )


def print_line(char='=', length=80):
    print(char[0:1] * length)


def print_xml(xml):
    xml_minidom = m.parseString(et.tostring(xml, encoding='utf8', method='xml'))
    print(xml_minidom.toprettyxml().strip())
    xml_minidom.unlink()


def xml_to_string(xml):
    return et.tostring(xml, method='xml').decode()

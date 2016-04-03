#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import six

print ('    |', end='')
[print("{0:3d}".format(i), end='') for i in six.moves.range(1, 10)]
print('\n ', end='')

for i in six.moves.range(1, 11):
    if (i == 2):
        print('+', end='')
    print('---', end='')
print()

for x in six.moves.range(1, 10):
    print("{0:3d}".format(x), '|', end='')
    for y in six.moves.range(1, 10):
        print("{0:3d}".format(x * y), end='')
    print()

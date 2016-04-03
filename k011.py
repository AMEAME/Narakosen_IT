#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import six

year = int(six.moves.input('何年(YYYY):'))
leap = 'うるう年' if (year % 4 == 0) and \
    (year % 100 != 0) or (year % 400 == 0) else '平年'
print(year, '年は', leap, 'です．')

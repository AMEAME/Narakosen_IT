#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import six

last_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year_month = six.moves.input('何年月: ').split('/')
h, y, m, t = int(year_month[0][0:1]), int(year_month[0][2:3]), int(year_month[1]), []
w = (y + y // 4 + h // 4 - 2 * h + 13 * (m + 1) // 5) % 7

[t.append(' ') for i in six.moves.range(0, w)]
[t.append(i) for i in six.moves.range(1, last_days[m - 1] + 1)]
print("   ", year_month[0], "年 ", int(year_month[1]), "月\n ", end='')
[print("{0} ".format(year_month), end='') for year_month in ["日", "月", "火", "水", "木", "金", "土"]]
print()
for n in six.moves.range(len(t)):
    if (n != 0) and (n % 7 == 0):
        print()
    if t[n] != ' ':
        print("{0:3d}".format(t[n]), end='')
    else:
        print("   ", end="")
print()

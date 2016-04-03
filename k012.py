#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import six

week = ['土', '日', '月', '火', '水', '木', '金']
date = six.moves.input('日時(YYYY/MM/DD):').split('/')

h, y = int(date[0][0:1]), int(date[0][2:3])
m, d = int(date[1]), int(date[2])

a = (y + (y // 4) + (h // 4) - (2 * h) + (13 * (m + 1) // 5) + d) % 7
print(date[0], '年', date[1], '月', date[2], '日は「', week[int(a)], '曜日」です．')

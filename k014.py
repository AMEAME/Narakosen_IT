#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import six
import datetime

s = six.moves.input('開始日 (YYYY/MM/DD): ').split('/')
e = six.moves.input('終了日 (YYYY/MM/DD): ').split('/')
a = datetime.date(int(e[0]), int(e[1]), int(e[2]))
b = datetime.date(int(s[0]), int(s[1]), int(s[2]))
print('日数差: ', (a - b).days, '日')

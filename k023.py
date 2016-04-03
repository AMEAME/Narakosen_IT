#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import six

data_file, rule = six.moves.input('Data file: '), int(six.moves.input('Rule (昇順：0, 降順:1): '))
t = {}

for line in open(data_file):
    t[line.rstrip()] = line[12:18]

if rule == 0:
    [print(k) for k, v in sorted(t.items(), key=lambda x: x[1])]
elif rule == 1:
    [print(k) for k, v in sorted(t.items(), key=lambda x: x[1])[::-1]]

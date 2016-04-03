#!/usr/bin/env python
# -*- coding: utf-8 -*-
import six
import random

year, month = '2015', 'Aug'
recoad_style = '{0}/{1}/{2:02d} {3:2.3f}'
output_file = open('temperature.dat', 'w')
for day in six.moves.range(1, 32):
    t = random.uniform(30.0, 40.0)
    output_file.write(recoad_style.format(
        year, month, day, t) + '\n')
    day += 1

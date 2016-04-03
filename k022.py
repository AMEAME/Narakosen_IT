#!/usr/bin/env python
# -*- coding: utf-8 -*-
n, sum, max, min, max_date, min_date = 0, 0, 0, float('inf'), '', ''

for line_data in open("temperature.dat"):
    daily_data = line_data.split()
    te = float(daily_data[1])
    if max < te: max, max_date = (te, daily_data[0]) 
    if min > te: min, min_date = (te, daily_data[0]) 
    sum += te
    n += 1

with open("average.dat", 'w') as w_file:
    w_file.write("日時: " + max_date + ", 最高気温: " + str(max) + " ℃\n")
    w_file.write("日時: " + min_date + ", 最低気温: " + str(min) + " ℃\n")
    w_file.write("平均気温: " + "{0:.3f}".format(sum / n) + " ℃\n")

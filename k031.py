#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

file1, file2, file3 = [], [], []

[file1.append(line) for line in open(sys.argv[1])]
[file2.append(line) for line in open(sys.argv[2])]


for line1 in file1:
    for line2 in file2:
        line1 = line1.replace(line2, '')
    file3.append(line1)

with open('result.dat', 'w') as file:
    [file.write(line) for line in file3]

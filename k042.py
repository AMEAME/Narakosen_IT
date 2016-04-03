#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re

txt, tr, td = [], False, []

for line in open(sys.argv[1]):
    if "</tr>\n" in line:
        tr = False
        if len(td) != 0: txt, td = (txt + [td], []) 
    if tr and line != "":
        td.append(re.sub(r'[(</td>)(<td>)(\n) ]', '', line))
    if "<tr>\n" in line: tr = True 

with open(sys.argv[2], 'w') as file:
    for line in txt:
        for i, word in enumerate(line):
            file.write(word + ("\n" if i == len(line) - 1 else ','))

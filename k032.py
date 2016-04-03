#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
if len(sys.argv) <= 2: exit(1);
o, l, con = open, len, ''

for file in range(1, l(sys.argv) - 1):
    w, a, li = 0, 0, 0
    
    for line in o(sys.argv[file]):
        a += l(line) + 1
        w += l(line.rstrip().split(' '))
        li = li + 1
    
    con += (sys.argv[file] + ":	" + str(w) +
            '文字, ' + str(a - 1) +
            '語, ' + str(li) + "行\n")

o(sys.argv[l(sys.argv) - 1], 'w').write(con)

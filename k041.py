#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

html= "<table>\n"
for rows in open(sys.argv[1]):
    html += "    <tr>\n"
    for word in rows.replace("\n", '').split(','):
        html += "        <td>" + word + "</td>\n"
    html += "    </tr>\n"
html += "</table>\n"

open(sys.argv[2], 'w').write(html)

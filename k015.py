#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import six
import datetime

in1 = six.moves.input('開始時間 (HH:MM):').split(':')
in2 = six.moves.input('終了時間 (HH:MM):').split(':')
t = datetime.time(int(in2[0]) - int(in1[0]), int(in2[1]) - int(in1[1]), 0)
print('経過時間: ', t.hour, '時間', t.minute, '分')

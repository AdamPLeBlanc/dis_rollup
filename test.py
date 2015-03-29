#! /usr/bin/env python

from dis_rollup import *

confFile = '/home/adam/Python_Course/dis_rollup/dis_rollup.conf'

ruMap = rollupmapper(confFile)

t1 = '1.3.5.2.5.6.7'
t2 = '1.2.255.1.5.6.7'
t3 = '2.2.3.4.5.6.7'
print ruMap.getRollup(t1)
print ruMap.getRollup(t2)
print ruMap.getRollup(t3)
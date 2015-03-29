#! /usr/bin/env python

import sys

class rollupmapper(object):
    _dpNum = 7
    _all = '*'
    _comment = '#'
    def __init__(self,confFileLoc):
        self.ruMap = {}
        for line in [l.strip() for l in open(confFileLoc,'rb')]:
            if line and line[0] != self._comment:
                dis,ru = line.split()
                disparts = dis.split('.')
                disparts += [self._all] * (self._dpNum - len(disparts))
                self._maprollup(disparts,self.ruMap,ru)
                    
    def getRollup(self,disEnum):
        disParts = disEnum.split('.')
        retVal = None
        if len(disParts) == self._dpNum:
            tmp = self.ruMap
            for dp in disParts:
                if tmp:
                    tmp = tmp.get(dp,tmp.get(self._all,None))
                    retVal = tmp
        return retVal
    
    def _maprollup(self,disparts,dismap,ru):
        vals = []
        dp = disparts[0]
        for v in dp.split(','):
            try:
                min,max = map(int,v.split('-'))
                if min < max:
                    vals += map(str,range(min,max+1))
            except ValueError:
                vals.append(v)
        for val in vals:
            tmpmap = dismap.get(val,{})
            if len(disparts) > 1:            
                self._maprollup(disparts[1:],tmpmap,ru)
                dismap[val] = tmpmap
            else:
                dismap[val] = ru
                        

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:02:25 2017

@author: Boheimain
"""

#淘汰
def calfitValue(obj_value):
    l=len(obj_value)
    fit_value = [0.0]*l
    for i in range(l):
        fit_value[i] = 1-obj_value[i]

    return fit_value
   
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:51:38 2017

@author: Boheimain
"""
import random


def geneEncoding(pop_size,chorm_length):
    pop = [[]]
    for i in range(pop_size):
        temp = []
        for j in range(chorm_length):
            temp.append(random.random())
        pop.append(temp)
    return pop[1:]

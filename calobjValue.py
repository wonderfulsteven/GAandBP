# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:55:28 2017

@author: Boheimain
"""

from BP_NN import NN



def calobjValue(pop,chrom_length,chrom_sites,inputs,targets):
    xi = chrom_sites[0]
    xh = chrom_sites[1]
    xo = chrom_sites[2]
    n = NN(xi,xh,xo)
    for i in range(len(pop)):
        x = 0
        error = []
        for j in range(xi):
            for k in range(xh):
                n.wi[j][k] = pop[i][x]
                x+=1
        for a in range(xh):
            for b in range(xo):
                n.wo[a][b] = pop[i][x]
                x+=1
        wi = n.wi
        wo = n.wo
        y=0.0
        for n in range(len(inputs)):
            p=inputs[n]
            q=targets[n]
            y+= n.sumError(p,q,wi,wo)
        error.append(y)
   
            
        
    return error
    
    
    
  
        
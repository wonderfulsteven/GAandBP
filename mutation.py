# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:07:39 2017

@author: Boheimain
"""

# 0.0 coding:utf-8 0.0  
# 基因突变  
  
import random  
  
  
def mutation(pop, pm):  
    px = len(pop)  #种群的总数
    py = len(pop[0])  #单个染色体（权值矩阵）的长度
      
    for i in range(px):  #种群的每个染色体都有机会变异
        if(random.random() < pm):  #如果产生的随机数小于变异概率
            mpoint = random.randint(0, py-1)  #随机选取一个变异的基因，即权值
            pop[i][mpoint]+= 0.1#发生变异的权值加上0.1
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:51:01 2017

@author: Boheimain
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:35:08 2017

@author: Boheimain
"""
from calfitValue import calfitValue  
from selection import selection  
from crossover import crossover  
from mutation import mutation  
from best import best  
import matplotlib.pyplot as plt

import random  
import math
import xlrd

def makeMatrix(I, J, fill=0.0):  #生成一个矩阵，元素全部为零，之后才为其赋值
    m = []  
    for i in range(I):  
        m.append([fill]*J)  
    return m  
  
# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)  
#使用双正切函数代替logistic函数  
def sigmoid(x):  
    return math.tanh(x)  


def geneEncoding(pop_size,chorm_length):
    pop = [[]]
    for i in range(pop_size):
        temp = []
        for j in range(chorm_length):
            temp.append(random.random())
        pop.append(temp)
    return pop[1:]


        

def cal_error_single(pop_code,chrom_length,chrom_sites,patterns):#计算某个输入特征值在中群下的误差
    xi = chrom_sites[0]
    xh = chrom_sites[1]
    xo = chrom_sites[2]
    wi=makeMatrix(xi,xh)
    wo=makeMatrix(xh,xo)
           
    x = 0
    for i in range(xi):
        for k in range(xh):
                wi[i][k] = pop_code[x]
                x+=1
    for a in range(xh):
        for b in range(xo):
            wo[a][b] = pop_code[x]
            x+=1
       
    
    error = 0.0  
    for p in patterns:  
        inputs = p[0]  
        targets = p[1]
        ai=[0.0]*xi
        ah=[0.0]*xh
        ao=[0.0]*xo
        for i in range(len(inputs)):  
             
            #self.ai[i] = sigmoid(inputs[i])  
            ai[i] = inputs[i]  
  
        # hidden activations  
        #隐藏层的激活函数,求和然后使用压缩函数  
        for j in range(xh):  
            sum = 0.0  
            for i in range(xi):  
                #sum就是《ml》书中的net  
                sum = sum + ai[i] * wi[i][j]  
            ah[j] = sigmoid(sum)  
  
        # output activations  
        #输出的激活函数  
        for k in range(xo):  
            sum = 0.0  
            for j in range(nh):  
                sum = sum + ah[j] * wo[j][k]  
            ao[k] = sigmoid(sum)  
  
 #       return self.ao[:]  
        
        error = error + 0.5*(targets[0]-ao[0])**2 
        
        

        
    return error

def calobjValue(pop,chrom_length,chrom_sites,patterns):
    error = []
    for i in range(len(pop)):
        pop_code = pop[i]
        y=cal_error_single(pop_code,chrom_length,chrom_sites,patterns)
        error.append(y)
    return error
  #打开Excel文件读取数据
data = xlrd.open_workbook('E:/textone.xlsx')
  
    #获取一个工作表
table = data.sheets()[0]          #通过索引顺序获取
  
table = data.sheet_by_index(0) #通过索引顺序获取
table = data.sheet_by_name('Sheet1')#通过名称获取
table1= data.sheet_by_name('Sheet2')
 # 获取行数和列数　
nrows = table.nrows
ncols = table1.nrows

 

#获取整行和整列的值（数组） 　　
inputs=[]
for i in range(nrows):
    inputs.append(table.row_values(i))
targets=[]
for j in range(ncols):
    targets.append(table1.row_values(j))
patterns=[0.0]*nrows
for k in range(nrows):
    add=[]
    add.append(inputs[k])
    add.append(targets[k])
    patterns[k]=add

ni=len(inputs[0])
no=len(targets[0])
nh=13   
chrom_sites = [ni,nh,no]#存储各层的神经网络节点数 
 

pop_size = 300 #种群数量
#max_value =10  基因允许出现的最大值，这里需要调整
chrom_length = ni*nh + nh*no#长度即为权值的个数
#其实这里可以用一个列表来分别表示[[ni*nh],[nh*no]]
pc = 0.6 #交配概率
pm = 0.01#变异概率
results = [[]]#存储每一代的最优解
fit_value = []#个体适应度
fit_mean = []#平均适应度
generation = 1000 #迭代多少代    
pop = geneEncoding(pop_size,chrom_length)

for i in range(generation):
  #  for i in range(pop_size):  
    obj_value = calobjValue(pop,chrom_length,chrom_sites,patterns)  
    
    fit_value = calfitValue(obj_value)      # 淘汰  
    best_individual, best_fit = best(pop, fit_value)        # 第一个存储最优的解, 第二个存储最优基因  
    results.append([best_fit])  
    selection(pop, fit_value)       # 新种群复制  
    crossover(pop, pc)      # 交配  
    mutation(pop, pm) 

X = []
Y = []
for i in range(500):
	X.append(i)
	t = results[i][0]
	Y.append(t)

plt.plot(X, Y)

plt.show()
#print results[1000][0]
'''

     # 个体差错 
    fit_value = calfitValue(obj_value)      # 淘汰  
    best_individual, best_fit = best(pop, fit_value)        # 第一个存储最优的解, 第二个存储最优基因  
   # results.append([best_fit])  
    selection(pop, fit_value)       # 新种群复制  
    crossover(pop, pc)      # 交配  
    mutation(pop, pm)       # 变异  
  
#results = results[1:]  
#results.sort()  
'''
 
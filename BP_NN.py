# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 09:07:29 2017

@author: Boheimain
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:49:31 2017

@author: Boheimain
"""

# Back-Propagation Neural Networks  
#   
  
import math  
import random  
#import string  
 #import untitled1  在同一个文件夹下就可以找到
random.seed(0)  
  
# calculate a random number where:  a <= rand < b  
def rand(a, b):  
    return (b-a)*random.random() + a  
  
# Make a matrix (we could use NumPy to speed this up)  
def makeMatrix(I, J, fill=0.0):  #生成一个矩阵，元素全部为零，之后才为其赋值
    m = []  
    for i in range(I):  
        m.append([fill]*J)  
    return m  
  
# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)  
#使用双正切函数代替logistic函数  
def sigmoid(x):  
    return math.tanh(x)  
  
# derivative of our sigmoid function, in terms of the output (i.e. y)  
# 双正切函数的导数，在求取输出层和隐藏侧的误差项的时候会用到  
def dsigmoid(y):  
    return 1.0 - y**2  
  
class NN:  
    def __init__(self, ni, nh, no):  
        # number of input, hidden, and output nodes  
        # 输入层，隐藏层，输出层的数量，三层网络  
        self.ni = ni #  输入层节点数
        self.nh = nh     #隐含层节点数
        self.no = no     #输出层节点数
  
        # activations for nodes  
        self.ai = [1.0]*self.ni  #输入层激活值列表
        self.ah = [1.0]*self.nh  #隐含层激活值列表
        self.ao = [1.0]*self.no  #输出层激活值列表
          
        # create weights  
        #生成权重矩阵，每一个输入层节点和隐藏层节点都连接  
        #每一个隐藏层节点和输出层节点链接  
        #大小：self.ni*self.nh  
        self.wi = makeMatrix(self.ni, self.nh)  # 输入层与隐含层之间权值矩阵
        #大小：self.ni*self.nh   
        self.wo = makeMatrix(self.nh, self.no)  #隐含层与输出层之间权值矩阵  
       

        # last change in weights for momentum   
        #?  
        self.ci = makeMatrix(self.ni, self.nh)  #保存最后的权值矩阵结果
        self.co = makeMatrix(self.nh, self.no)  #保存最后的权值矩阵结果New

    def sumError(self, inputs,targets,wi,wo):  
        if len(inputs) != self.ni:  
            raise ValueError('wrong number of inputs')  #检测输入列表是否正确
  
        # input activations  
        # 输入的激活函数，就是y=x;  
        for i in range(self.ni):  #把输入值赋给输入层的初始输入值
            #self.ai[i] = sigmoid(inputs[i])  
            self.ai[i] = inputs[i]  
  
        # hidden activations  
        #隐藏层的激活函数,求和然后使用压缩函数  
        for j in range(self.nh):  #求出隐含层的输入值和激活函数之后的输出值
            sum = 0.0  
            for i in range(self.ni):  
                #sum就是《ml》书中的net  
                sum = sum + self.ai[i] * self.wi[i][j]  #隐含层每一个节点的输入值
            self.ah[j] = sigmoid(sum)  #隐含层每一个节点的输出值
  
        # output activations  
        #输出的激活函数  
        for k in range(self.no):  
            sum = 0.0  
            for j in range(self.nh):  
                sum = sum + self.ah[j] * self.wo[j][k]  #输出层每一个节点的输入值
            self.ao[k] = sigmoid(sum)  #输出层每一个节点的输出值
  
       
        
        # calculate error  
        #计算E(w)  
        error = 0.0  
        for k in range(len(targets)):  
            error = error + 0.5*(targets[k]-self.ao[k])**2  
        return error  
  
  
   
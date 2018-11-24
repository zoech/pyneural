# -*- coding: UTF-8 -*-
import numpy as np
import random
#import math

import os

class NeuralNet:

    def __init__(self, inputDim=0, layersVec=[]):

        self.learningFactor = 3.0
        self.inDim = inputDim
        self.outDim = layersVec[len(layersVec) -1]
        self.layers = len(layersVec)
        
        self.w = []
        self.b = []

        for l in range(self.layers):
            thisNodes = layersVec[l] #当前层的神经元个数
            preNodes = inputDim if l == 0 else layersVec[l-1]

            #wt = np.zeros((thisNodes, preNodes)) # 权重矩阵，
            #bt = np.zeros(thisNodes) # 偏置向量

            # 不知道为什么！！初始化为正态分布简直太有效了！！
            wt = np.random.randn(thisNodes, preNodes) # 权重矩阵，
            bt = np.random.randn(thisNodes) # 偏置向量

            self.w.append(wt)
            self.b.append(bt)


    # 学习率
    def setLearningFac(self, fac):
        self.learningFactor = fac

        
    def raw_predict(self, iv):
        if len(iv) != self.inDim:
            print("incompatible input dimention! only " + str(self.inDim) + " vectors!")
        
        z = np.array(iv)
        for l in range(self.layers):
            z = np.dot(self.w[l], z)
            z = z + self.b[l]
            self.do_sigmoid(z)


        return z


    def predict(self, iv):
        ov = self.raw_predict(iv)
        return [k for k in ov].index(max(ov))
        

    def sigmoid(self, zi):
        return 1.0/(1.0+np.exp(-zi))


    def do_sigmoid(self, z):
        for i in range(len(z)):
            z[i] = self.sigmoid(z[i])



    def dump_w(self, path):
        wa = np.array(self.w)
        wa.dump(path)


    def dump_b(self, path):
        ba = np.array(self.b)
        ba.dump(path)


    def load_w(self, path):
        self.w = np.load(path)

    def load_b(self, path):
        self.b = np.load(path)

    def dump(self):
        self.dump_w('D:\\tmp\\neuralnet.wd')
        self.dump_b('D:\\tmp\\neuralnet.bd')


    def load_ori(self):
        self.load_w('D:\\tmp\\neuralnet.wd')
        self.load_b('D:\\tmp\\neuralnet.bd')
        self.inDim = len(self.w[0][0])




    ## 单次训练过程
    def training(self, iv, ov):
        #pv = self.raw_predict(iv)
        a = []
        z = np.array(iv)
        for l in range(self.layers):
            z = np.dot(self.w[l], z)
            z = z + self.b[l]
            self.do_sigmoid(z)
            a.append(np.array(z))

        # 以下计算每一层的w偏导和b偏导
        # 先求a = np.array([1,2,3],[4,5,6]) e / a[n] 偏导, 代价使用 1/2 * (a - y)^2
        e_a = a[self.layers-1] - ov # 即 z-ov, 上面计算之后，z即为最后输出，同时压入了a的最后面
        deri_ = e_a

        #print("\n\n==========================================")
        for i in range(self.layers-1, -1, -1): # 倒序
            a_z = a[i] * (1 - a[i])
            z_w = np.array(iv) if i == 0 else a[i-1]
            
            e_z = deri_ * a_z
            e_w = np.array([z_w * x for x in e_z]) # 权重偏导
            e_b = e_z # 偏置偏导

            #if not e_w.any():
                #print('layers:' + str(i) + ' e_w zero')


            # 更新权重和偏置
            self.w[i] = self.w[i] - self.learningFactor * e_w
            self.b[i] = self.b[i] - self.learningFactor * e_b


            # 求上一层输出a的偏导
            #deri_ = sum(self.w[i]) * sum(e_z)
            tmp = [ii * kk for (ii,kk) in zip(self.w[i], e_z)]
            deri_ = sum(tmp) / len(tmp)         # 这里z维度分散到上层a输入（相加后取均值，比较下求和的差别）

            #print(deri_)
            
            
        



def build_zero_neuralNet(inputDim, layersVec):
    net = NeuralNet(inputDim, layersVec)

    for l in range(net.layers):
        net.w[l] = net.w[l].dot(0)
        net.b[l] = net.b[l].dot(0)
        
    return net

def build_norm_neuralNet(inputDim, layersVec):
    return NeuralNet(inputDim,layersVec)


def random_net(net, min_v, max_v):
    for l in range(net.layers):

        for outVec in net.w[l]:

            for i in range(len(outVec)):
                outVec[i] = (max_v - min_v) * random.random() + min_v


        for i in range(len(net.b[l])):
            net.b[l][i] = (max_v - min_v) * random.random() + min_v



if __name__ == "__main__":
    net = build_zero_neuralNet(10, [20,56,40,55,20,44,22,10])
    random_net(net,0,1)
    #print(net.w[0])
    o = net.raw_predict([1,0,0,1,0,1,1,1,0,0])
    print(o)

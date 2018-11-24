# -*- coding: UTF-8 -*-

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math

import NeuralNet as Nnet

net = Nnet.build_norm_neuralNet(784, [30, 10])
net.load_ori()

def _load_jpeg(path):
    img = Image.open(path).convert('L')
    return img


def _norm_28_28(img):
    return img.resize((28,28))

def _get_vec_data(img):
    data = np.array(img) # 这个是28*28的二维数据
    data = (1-data) / 255.0 # 反相，并转为float数据
    data = data.reshape(28*28) # 转为一维
    return data


# 将灰度数据进行初步处理，提高辨识度
def _pre_process(data):
    fence = 0.5
    gap = (100, 150)

    for turn in range(5):
        t = 0
        for i in data:
            if i > fence:
                t = t+1

        if t < gap[0]:
            fence = fence - math.pow(0.5, turn+2.0)
        elif t > gap[1]:
            fence = fence + math.pow(0.5, turn+2.0)
        else:
            break

    l = len(data)
    for i in range(l):
        if data[i] < fence:
            data[i] = 0.0
        else:
            data[i] = 0.908

def figure(path):
    img = _load_jpeg(path)
    img = _norm_28_28(img)
    
    data = _get_vec_data(img)

    _pre_process(data)

    return net.predict(data)

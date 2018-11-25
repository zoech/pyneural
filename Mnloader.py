# -*- coding: UTF-8 -*-


import cPickle
import gzip
import numpy as np

import os


def load_data_raw(path):

    f = gzip.open(path,'rb')
    tr_d, v_d, test_d = cPickle.load(f)
    f.close()
    return (tr_d, v_d, test_d)


def load_data(path):
    tr_d, va_d, te_d = load_data_raw(path)
    #training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(tr_d[0], tr_d[1])
    #training_data = zip(tr_d[0], tr_d[1])

    #validation_results = [vectorized_result(y) for y in va_d[1]]
    #validation_data = zip(va_d[0], validation_results)
    validation_data = zip(va_d[0], va_d[1])

    #test_results = [vectorized_result(y) for y in te_d[1]]
    #test_data = zip(te_d[0], test_results)
    test_data = zip(te_d[0], te_d[1])

    return (training_data, validation_data, test_data)


def convert2_training_data(v):
    res = []
    for ov in v:
        vres = vectorized_result(ov[1])
        res.append((ov[0],vres))
    
    return res


# 将数据分类导入，第一批数据转为训练数据
def load_data_classify(path):
    tr_d, va_d, te_d = load_data(path)
    tr_d = convert2_training_data(tr_d)
    return (tr_d,va_d,te_d)


def vectorized_result(j):
    """Return a 10-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a digit
    (0...9) into a corresponding desired output from the neural
    network."""
    e = np.zeros(10)
    e[j] = 1.0
    return e

# 将数据代表的数字图像可视化打印一下
def show_data_as_pic(v,fence=0.3):
    strGraph, num = get_data_graph(v)
    print(strGraph + '\n')
    print('active pixels : ' + str(num))


def get_data_graph(v,fence=0.3):
    num = 0
    strGraph = ''
    for line in range(28):
        lineStr = '';
        for y in range(28):
            if v[28*line + y] > fence :
                lineStr = lineStr + '$$'
                num = num + 1
            else:
                lineStr = lineStr +'..'
        #print(lineStr)
        lineStr = lineStr + os.linesep
        strGraph = strGraph + lineStr
    #print('active pixels : ' + str(num))

    return (strGraph,num)

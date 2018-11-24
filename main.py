# -*- coding: UTF-8 -*-
import NeuralNet as Nnet
import Mnloader as loader

def build_init_net():
    net = Nnet.build_norm_neuralNet(784, [30, 10])
    #Nnet.random_net(net, 0, 3.0)
    return net



def test_net(net, v_d):
    #tr_d, v_d, t_d = loader.load_data('d:\mnist.pkl.gz')

    total = 0.0
    correct = 0.0

    for item in v_d:
        total = total + 1.0
        predict = net.predict(item[0])
        if predict == item[1]:
            correct = correct + 1.0


    print('total: ' + str(total))
    print('right: ' + str(correct))
    print('percent: ' + str(correct/total))


def training_net_with_test(net, turns, trd, vd):
    l = len(trd)
    print("\n\n ------------------training -------------------")
    for x in range(turns):
        for i in range(l):
            net.training(trd[i][0], trd[i][1])

    print("\n\n ==================== testing ======================")
    test_net(net, vd)


if __name__ == '__main__':
    net = build_init_net()
    #print(net.w[0])
    tr_d, v_d, t_d = loader.load_data_classify('./data/mnist.pkl.gz')
    #net.training(tr_d[0][0], tr_d[0][1])

    #for i in range(5000):
        #net.training(tr_d[i][0], tr_d[i][1])

'''
    print(net.predict(v_d[0][0]))
    print(v_d[0][1])

    print(net.predict(v_d[22][0]))
    print(v_d[22][1])
'''

    

# pyneural

一个神经网络的小练习，用于识别手写数字  

实现过程中主要了解这些：
反向传播  
权重的矩阵表示，理解矩阵变换线性变换，加深矩阵变换输入输出的视觉印象


### 依赖
* python2.7
* libjpeg
* python2.7 PIL 模块
* pyqt5 模块

### 测试
#### 跑 main.py 模块（idle命令交互）
* net.load_ori() 可以加载上次net.dump()保存的默认的神经网
* net.dump() 可以将当前网络net保存到默认的路径
* 下面代码（或者在idle里交互输入)将网络训练一遍：
```python
for i in range(len(tr_d)):
  net.training(tr_d[i][0],tr_d[i][1])
```
* test_net(net, v_d)  可以使用数据集  v_d 来测试 当前网络net的正确率

#### 跑 MainWindow.py模块（窗口）
这个ui做的比较简单，窗口和截屏的代码都是网上随便找来改的，大概的过程如下：

* ScreenShooter截屏存为临时文件(pyqt5);;
* JpegHandler将截图转为一维数据(PIL);
* JpegHandler预处理(图片很白两极分化);
* 调用NeuralNet.predict();

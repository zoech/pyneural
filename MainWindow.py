# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMessageBox)
from PyQt5.QtGui import QFont

import UI.ScreenShooter as sShoot

##sys.path.append("..")
import JpegHandler as jpghandler
import Mnloader as loader
#from PyQt5.QtCore import QCoreApplication


#def figure(widget):
    #print('figure')
    #QMessageBox.information(widget,'hello', 'hi')

def screenshot(path,parent):
    sShoot.WScreenShot.run(path)#,parent)
    
 
class Example(QWidget):
     
    def __init__(self):
        super(Example, self).__init__()

        self.tmp_jpg_file = '/home/zoey/tmp/screenshoot_xx.jpg'
         
        self.initUI()
         
         
    def initUI(self):
         
        QToolTip.setFont(QFont('SansSerif', 10))
         
        self.setToolTip('This is a widget')
         
        btn = QPushButton('figure', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.clicked.connect(self.figure_rec)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)      
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Digit Recognition')   
        self.show()

    def figure_rec(self):
        #self.hide()
        #print('figure')
        sShoot.WScreenShot.run(self.tmp_jpg_file, self)
        #screenshot(self.tmp_jpg_file,self)
        #x = jpghandler.figure(tmp_jpg_file)
        #QMessageBox.information(self,'hello', 'jj')
        #self.show()

    def shooter_callback(self):
        #print('callback')
        x,pro_d,fence = jpghandler.figure(self.tmp_jpg_file)
        print("\n\n======== data graph ==========\n")
        print(loader.get_data_graph(pro_d,fence)[0])
        QMessageBox.information(self,'res', str(x))
        #QMessageBox.information(self,'graph', loader.get_data_graph(pro_d)[0])
         
if __name__ == '__main__':
     
    app = QApplication.instance() or QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

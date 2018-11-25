# -*- coding: utf-8 -*-
#from PyQt5 import __binding__
#print( __binding__)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
'''
# Qt 中无法导入 QScreen 类
try:
    from PySide2.QtGui import QScreen
except:
    from PyQt5.QtGui import QScreen
'''
import sys



class WScreenShot(QWidget):
    
    win = ''
    
    @classmethod
    def run(cls, path, ss_parent__=None):
        cls.win = cls(path,ss_parent__)
        cls.win.show()
    
    def __init__(self, out_path = './py_screenshot_.jpg',ss_parent_ = None, parent = None):
        super(WScreenShot, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:black; ''')
        self.setWindowOpacity(0.6)
        # desktop = QApplication.desktop()
        # rect = desktop.availableGeometry()
        desktopRect = QDesktopWidget().screenGeometry()
        self.setGeometry(desktopRect)
        self.setCursor(Qt.CrossCursor)
        self.blackMask = QBitmap(desktopRect.size())
        self.blackMask.fill(Qt.black)
        self.mask = self.blackMask.copy()
        self.isDrawing = False
        self.startPoint = QPoint()
        self.endPoint = QPoint()

        self.path = out_path
        self.ss_parent = ss_parent_

    def paintEvent(self, event):
        if self.isDrawing:  
            self.mask = self.blackMask.copy()
            pp = QPainter(self.mask)
            pen = QPen()
            pen.setStyle(Qt.NoPen) 
            pp.setPen(pen)
            brush = QBrush(Qt.white)
            pp.setBrush(brush)
            pp.drawRect(QRect(self.startPoint, self.endPoint))
            self.setMask(QBitmap(self.mask))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = self.startPoint
            self.isDrawing = True
        
    def mouseMoveEvent(self, event):
        if self.isDrawing:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # PySide2
            #screenshot = QPixmap.grabWindow(QApplication.desktop().winId())
            # PyQt5
            #screenshot = QApplication.primaryScreen().grabWindow(0)
            # 通用
            screenshot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
            rect = QRect(self.startPoint, self.endPoint)
            outputRegion = screenshot.copy(rect)
            outputRegion.save(self.path, format = 'JPG', quality = 100)

            self.close()
            if self.ss_parent != None and self.ss_parent.shooter_callback != None:
                self.ss_parent.shooter_callback()
                
            

if __name__ == '__main__':
    app = QApplication.instance() or QApplication(sys.argv)
    WScreenShot.run('./ttt.jpg')
    app.exec_()

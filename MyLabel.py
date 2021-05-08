from PyQt5.QtGui import QPen, QPainter, QColor
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore, QtWidgets
import sys


class MyLabel(QLabel):
    rect = None

    def __int__(self):
        super(MyLabel, self).__init__()

    # 重写绘制函数
    def paintEvent(self, event):
        # 初始化绘图工具
        qp = QPainter()
        # 开始在窗口绘制
        qp.begin(self)
        # 自定义画点方法
        if self.rect:
            self.drawRect(qp)
        # 结束在窗口的绘制
        qp.end()

    def drawRect(self, qp):
        # 创建红色，宽度为4像素的画笔
        pen = QPen(QColor(0, 255, 0), 2)
        qp.setPen(pen)
        qp.drawRect(*self.rect)

    # 重写三个时间处理
    def mousePressEvent(self, event):
        print("mouse press")
        self.rect = (event.x(), event.y(), 0, 0)
        print(event.x(), event.y())

    def mouseReleaseEvent(self, event):
        print(event.x(), event.y())
        print("mouse release")

    def mouseMoveEvent(self, event):
        start_x, start_y = self.rect[0:2]
        self.rect = (start_x, start_y, event.x() - start_x, event.y() - start_y)
        self.update()

    def getData(self):
        return self.rect


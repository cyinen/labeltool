from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPen, QPainter, QColor
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore, QtWidgets


class MyLabel(QLabel):
    sendDataSig = pyqtSignal(list)

    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.setWindowTitle('拖拽绘制矩形')
        self.rect = None
        self.textEdit = QtWidgets.QLineEdit(self)
        self.textEdit.setHidden(True)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, False)
        self.textEdit.returnPressed.connect(self.getData)

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
        pen = QPen(QColor(0,255,0), 2)
        qp.setPen(pen)
        qp.drawRect(*self.rect)

    # 重写三个时间处理
    def mousePressEvent(self, event):
        self.rect = (event.x(), event.y(), 0, 0)

    def mouseReleaseEvent(self, event):
        if not self.rect:
            return
        if self.rect[0] == event.x():
            return
        self.textEdit.setGeometry(QtCore.QRect(event.x(), event.y(), 200, 50))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.show()

    def mouseMoveEvent(self, event):
        start_x, start_y = self.rect[0:2]
        self.rect = (start_x, start_y, event.x() - start_x, event.y() - start_y)
        self.update()

    def getData(self):
        strs = self.textEdit.text()
        self.textEdit.clear()
        self.sendDataSig.emit([self.rect, strs])
        self.textEdit.setHidden(True)
        # return self.rect, strs

from PyQt5 import QtCore
from PyQt5.QtGui import QPolygon
from PyQt5.QtCore import Qt, QPoint
from sys import argv, exit
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from random import choice, randint


class Suprematism(QMainWindow):
    def setupUi(self, Form):
        self.setMouseTracking(True)
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        trans = QtCore.QCoreApplication.translate
        Form.setWindowTitle(trans("Form", "Form"))

    def __init__(self):
        super().__init__()
        self.flag = 0
        uic.loadUi('Ui.ui', self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)

 
    def draw(self, qp):
        if self.flag:
            qp.setBrush(QColor('Yellow'))
            leigt = randint(50, 200)
            qp.drawEllipse(randint(0, 600), randint(0, 400), leigt, leigt)

    def paint(self):
        self.flag = 1
        self.update()


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Suprematism()
    ex.show()
    exit(app.exec())

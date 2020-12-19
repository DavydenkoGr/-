import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.rep)

    def rep(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.run(qp)
        qp.end()

    def run(self, qp):
        qp.setPen(QColor(255, 255, 0))
        n = randint(20, 250)
        qp.drawEllipse(278 - n // 2, 278 - n // 2 , n, n)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
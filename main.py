import sys
import random

from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
lst = []
count = 0


class DrawStar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('task 3')
        self.pushButton = QPushButton("ЖМИ!!!!!!!!!", self)
        self.pushButton.resize(231, 51)
        self.pushButton.move(280, 200)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_star(qp)
            qp.end()

    def paint(self):
        global count
        self.do_paint = True
        self.repaint()
        count += 1

    def draw_star(self, qp):
        global count
        global lst
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        wh = random.randint(0, 500)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        lst.append([x, y, wh, r, g, b])
        lst = lst[:count + 1]
        for i in lst:
            pen = QPen(QColor(i[3], i[4], i[5]), 5)
            qp.setPen(pen)
            qp.drawArc(i[0], i[1], i[2], i[2], 0, 5760)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec())

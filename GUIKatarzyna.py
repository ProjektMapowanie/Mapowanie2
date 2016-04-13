# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIKatarzyna.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import math as m


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyWidget(QtGui.QWidget):

    def __init__(self, parent):
        QtGui.QWidget.__init__(self)
        self.setParent(parent)
        self.show()
        self.trace = []
        self.x = 100
        self.y = 100
        self.theta = 0
        self.a = 40
        self.keys = [False, False, False, False]

        a =  [[200, 100], [205, 110], [211, 122], [217, 120], [221, 125], [224, 130], [225, 127],
                          [224, 130], [225, 132], [231, 132], [237, 135], [238, 135], [244, 138], [245, 137],
                          [246, 138], [246, 138], [242, 142], [227, 145], [245, 145], [251, 148], [252, 147]]
        self.landmarks = a
        

    def showEvent(self, event):
        self.timer = self.startTimer(30)

    def timerEvent(self, event):
        if self.keys[0]:
            self.theta -= 2
        elif self.keys[1]:
            self.theta += 2
        if self.keys[2]:
            self.x += 2*m.sin(self.theta*m.pi/180)
            self.y -= 2*m.cos(self.theta*m.pi/180)
        elif self.keys[3]:
            self.x -= 2*m.sin(self.theta*m.pi/180)
            self.y += 2*m.cos(self.theta*m.pi/180)
        self.trace.append([self.x, self.y])
        self.update()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRobot(qp)
        self.drawLandmarks(qp)
        qp.end()


    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Left:
            self.keys[0] = True
        elif e.key() == QtCore.Qt.Key_Right:
            self.keys[1] = True
        if e.key() == QtCore.Qt.Key_Up:
            self.keys[2] = True
        elif e.key() == QtCore.Qt.Key_Down:
            self.keys[3] = True

    def keyReleaseEvent(self, e):
        if e.key() == QtCore.Qt.Key_Left:
            self.keys[0] = False
        elif e.key() == QtCore.Qt.Key_Right:
            self.keys[1] = False
        if e.key() == QtCore.Qt.Key_Up:
            self.keys[2] = False
        elif e.key() == QtCore.Qt.Key_Down:
            self.keys[3] = False

    def leastSquares(self, landmarks):
        Exy = Ex = Ey = Ex2 = 0
        for sth in landmarks:
            Exy = Exy + sth[0]*sth[1]
            Ex = Ex + sth[0]
            Ey = Ey + sth[1]
            Ex2 = Ex2 + sth[0]**2

        n = len(self.landmarks)
        a = (n*Exy - Ex*Ey)/(n*Ex2 - Ex**2)
        b = Ey/n - a*Ex/n

        return [a, b]


    def drawLandmarks(self, qp):


        for sth in self.landmarks:
            qp.drawPoint(sth[0],   sth[1])

        a, b = self.leastSquares(self.landmarks)
        x0 = self.landmarks[0][0]
        y0 = a*x0 + b

        x1 = 500
        y1 = a*x1 + b


        qp.drawLine(x0, y0, x1, y1)


        #qp.drawPoint(160,   61)
        #qp.drawPoint(160,   62)
        #qp.drawPoint(160,   63)
        #qp.drawPoint(160,   64)

        #for i in self.landmarks:
        #    print("o")
        #    qp.drawPoint(i[0], i[1], '*')

    def drawRobot(self, qp):
        qp.setPen(QtCore.Qt.blue)
        for i in self.trace:
            qp.drawPoint(i[0], i[1])
        qp.setBrush(QtCore.Qt.red)
        qp.translate(self.x, self.y)
        qp.rotate(self.theta)
        #qp.drawRect(-self.width/2, -self.height/2, 40, 40)
        qp.drawPolygon(QtCore.QPoint(0, -self.a*m.sqrt(3)/3), QtCore.QPoint(-self.a/2, self.a*m.sqrt(3)/6), QtCore.QPoint(self.a/2, self.a*m.sqrt(3)/6))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(811, 591)
        self.widget = MyWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 20, 771, 551))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.widget.setFocus()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


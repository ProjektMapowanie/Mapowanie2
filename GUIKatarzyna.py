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

        pion = [[300, 300], [300, 303], [300, 307], [302, 312], [300, 313], [301, 320], [300, 322], [300, 326],
             [300, 328], [300, 331], [301, 335], [300, 340], [300, 345]]

        ab = [[300, 300], [300, 303], [300, 307], [302, 312], [300, 313], [301, 320], [300, 322], [300, 326],
             [300, 328], [300, 331], [301, 335], [300, 340], [300, 345],
             [200, 100], [205, 110], [211, 122], [217, 120], [221, 125], [224, 130], [225, 127],
             [224, 130], [225, 132], [231, 132], [237, 135], [238, 135], [244, 138], [245, 137],
             [246, 138], [246, 138], [242, 142], [227, 145], [245, 145], [251, 148], [252, 147],
              [253, 144], [255, 142], [256, 140], [257, 135], [260, 133], [260, 128], [263, 125],
              [265, 124], [270, 122], [273, 120], [277, 116], [277, 107], [279, 118], [280, 108]]

        b = [[200, 100], [205, 110], [211, 122], [217, 120], [221, 125], [224, 130], [225, 127],
                         [224, 130], [225, 132], [231, 132], [237, 135], [238, 135], [244, 138], [245, 137],
                          [246, 138], [246, 138], [242, 142], [227, 145], [245, 145], [251, 148], [252, 147]]

        drugaStrona = [[253, 144], [255, 142], [256, 140], [257, 135], [260, 133], [260, 128], [263, 125],
              [265, 124], [270, 122], [273, 120], [277, 116], [277, 107], [279, 118], [280, 108]]

        d = [[253, 144], [255, 142], [256, 140], [261, 135] ]#[[200, 200], [150, 170], [110, 130]]
        f = [[200, 200], [208, 197], [211, 196], [210, 194], [208, 193]]

        self.landmarks = b


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
        self.drawLandmarks(qp)
        self.drawRobot(qp)
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

        if landmarks[0][0] - landmarks[len(landmarks) - 1][0] < 0:
            a = a

        return [a, b]

    def paintLandGroup(self, landmarks, qp):
        a, b = self.leastSquares(landmarks)
        x0 = landmarks[0][0]
        x = landmarks[0]
        vv = landmarks[len(landmarks)- 1]
        if a < 0.1:

            y0 = landmarks[0][1]
            x1 = landmarks[len(landmarks) - 1][0]
            y1 = landmarks[len(landmarks) - 1][1]
        else:
            y0 = a*x0 + b

            x1 = landmarks[len(landmarks) - 1][0]
            y1 = a*x1 + b



        qp.drawLine(x0, y0, x1, y1)

    def closersPoint(self, point, helpfull_list):
        pLists = []
        for lm in helpfull_list:
            if m.sqrt((point[0] - lm[0])**2 + (point[1] - lm[1])**2) < 10:
                w = m.sqrt((point[0] - lm[0])**2 + (point[1] - lm[1])**2)
                pLists.append(lm)
                helpfull_list.remove(lm)
            if len(pLists) > 10:
                break
        return pLists

        pass


    def drawLandmarks(self, qp):

        helpfull_list = self.landmarks.copy()
        for sth in helpfull_list:
            qp.drawPoint(sth[0],   sth[1])
            if len(helpfull_list) > 2:
                pList = self.closersPoint(sth, helpfull_list)
                self.paintLandGroup(pList, qp)
            self.paintLandGroup(self.landmarks, qp)

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


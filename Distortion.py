from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 276)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 811, 341))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0.833698, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 250, 231, 255));\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 10, 281, 81))
        self.label.setStyleSheet("font: 26pt \"ROG Fonts\";\n"
"color:grey;")
        self.label.setObjectName("label")
        self.dial = QtWidgets.QDial(self.widget)
        self.dial.valueChanged.connect(self.clicked4)
        self.dial.setMinimum(0)
        self.dial.setMaximum(99)
        self.dial.setGeometry(QtCore.QRect(80, 100, 50, 64))
        self.dial.setObjectName("dial")
        self.dial_2 = QtWidgets.QDial(self.widget)
        self.dial_2.valueChanged.connect(self.clicked5)
        self.dial_2.setMinimum(0)
        self.dial_2.setMaximum(99)
        self.dial_2.setGeometry(QtCore.QRect(200, 100, 50, 64))
        self.dial_2.setObjectName("dial_2")
        self.dial_3 = QtWidgets.QDial(self.widget)
        self.dial_3.valueChanged.connect(self.clicked2)
        self.dial_3.setMinimum(0)
        self.dial_3.setMaximum(99)
        self.dial_3.setGeometry(QtCore.QRect(30, 180, 50, 64))
        self.dial_3.setObjectName("dial_3")
        self.dial_4 = QtWidgets.QDial(self.widget)
        self.dial_4.valueChanged.connect(self.clicked3)
        self.dial_4.setMinimum(0)
        self.dial_4.setMaximum(99)
        self.dial_4.setGeometry(QtCore.QRect(140, 180, 50, 64))
        self.dial_4.setObjectName("dial_4")
        self.dial_5 = QtWidgets.QDial(self.widget)
        self.dial_5.valueChanged.connect(self.clicked)
        self.dial_5.setMinimum(0)
        self.dial_5.setMaximum(99)
        self.dial_5.setGeometry(QtCore.QRect(250, 180, 50, 64))
        self.dial_5.setObjectName("dial_5")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(50, 70, 701, 40))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(320, 110, 31, 151))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(380, 100, 51, 31))
        self.label_2.setStyleSheet("font: 12pt \"Ravie\";\n"
"color:rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.dial_6 = QtWidgets.QDial(self.widget)
        self.dial_6.valueChanged.connect(self.clicked6)
        self.dial_6.setGeometry(QtCore.QRect(350, 130, 111, 121))
        self.dial_6.setObjectName("dial_6")
        self.dial_6.setMinimum(0)
        self.dial_6.setMaximum(99)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 81, 31))
        self.label_3.setStyleSheet("font: 10pt \"Ravie\";\n"
"color:rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(190, 150, 71, 31))
        self.label_4.setStyleSheet("font: 10pt \"Ravie\";\n"
"color:rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(120, 230, 101, 31))
        self.label_5.setStyleSheet("font: 10pt \"Ravie\";\n"
"color:rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 51, 31))
        self.label_6.setStyleSheet("font: 10pt \"Ravie\";\n"
"color:rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(250, 230, 91, 31))
        self.label_7.setStyleSheet("font: 10pt \"Ravie\";\n"
"color:rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.dial_7 = QtWidgets.QDial(self.widget)
        self.dial_7.valueChanged.connect(self.clicked7)
        self.dial_7.setMinimum(0)
        self.dial_7.setMaximum(99)
        self.dial_7.setGeometry(QtCore.QRect(480, 110, 81, 91))
        self.dial_7.setObjectName("dial_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(500, 210, 51, 31))
        self.label_8.setStyleSheet("font: 12pt \"Ravie\";\n"
"color:rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.dial_8 = QtWidgets.QDial(self.widget)
        self.dial_8.valueChanged.connect(self.clicked8)
        self.dial_8.setMinimum(0)
        self.dial_8.setMaximum(99)
        self.dial_8.setGeometry(QtCore.QRect(600, 150, 61, 81))
        self.dial_8.setObjectName("dial_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(610, 130, 51, 31))
        self.label_9.setStyleSheet("font: 12pt \"Ravie\";\n"
"color:rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.dial_9 = QtWidgets.QDial(self.widget)
        self.dial_9.valueChanged.connect(self.clicked9)
        self.dial_9.setMinimum(0)
        self.dial_9.setMaximum(99)
        self.dial_9.setGeometry(QtCore.QRect(720, 120, 41, 61))
        self.dial_9.setObjectName("dial_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(720, 170, 61, 31))
        self.label_10.setStyleSheet("font: 12pt \"Ravie\";\n"
"color:rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Distortion"))
        self.label_2.setText(_translate("Dialog", "Mix"))
        self.label_3.setText(_translate("Dialog", "Feedback"))
        self.label_4.setText(_translate("Dialog", "Release"))
        self.label_5.setText(_translate("Dialog", "Saturation"))
        self.label_6.setText(_translate("Dialog", "Drive"))
        self.label_7.setText(_translate("Dialog", "Cutoff"))
        self.label_8.setText(_translate("Dialog", "Tone"))
        self.label_9.setText(_translate("Dialog", "Gain"))
        self.label_10.setText(_translate("Dialog", "Color"))


    def clicked(self):
        value = self.dial_5.value()
        if value == value:
                self.label_7.setText(f"db: {str(value)}")
        else:
                pass
    def clicked2(self):
        value2 = self.dial_3.value()
        if value2 == value2:
                self.label_6.setText(f"db: {str(value2)}")
                self.label_6.adjustSize()
        else:
                pass
    def clicked3(self):
        value3 = self.dial_4.value()
        if value3 == value3:
                self.label_5.setText(f"db: {str(value3)}")
                self.label_5.move(140,230)
        else:
                pass
    def clicked4(self):
        value4 = self.dial.value()
        if value4 == value4:
                self.label_3.setText(f"db: {str(value4)}")
        else:
                pass
    def clicked5(self):
        value5 = self.dial_2.value()
        if value5 == value5:
                self.label_4.setText(f"db: {str(value5)}")
        else:
                pass
    def clicked6(self):
        value6 = self.dial_6.value()
        if value6 == value6:
                self.label_2.setText(f"db: {str(value6)}")
                self.label_2.move(380,106)
                self.label_2.adjustSize()
        else:
                pass
    def clicked7(self):
        value7 = self.dial_7.value()
        if value7 == value7:
                self.label_8.setText(f"db: {str(value7)}")
                self.label_8.adjustSize()
        else:
                pass
    def clicked8(self):
        value8 = self.dial_8.value()
        if value8 == value8:
                self.label_9.setText(f"db: {str(value8)}")
                self.label_9.adjustSize()
        else:
                pass
    def clicked9(self):
        value9 = self.dial_9.value()
        if value9 == value9:
                self.label_10.setText(f"db: {str(value9)}")
                self.label_10.adjustSize()
        else:
                pass
    def clicked10(self):
        value10 = self.dial_8.value()
        if value10 == value10:
                self.label_8.setText(f"db: {str(value10)}")
                self.label_8.adjustSize()
        else:
                pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

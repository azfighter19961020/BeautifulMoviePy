# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BeautifulMoviePy(object):
    def setupUi(self, BeautifulMoviePy):
        BeautifulMoviePy.setObjectName("BeautifulMoviePy")
        BeautifulMoviePy.resize(527, 594)
        self.title = QtWidgets.QLabel(BeautifulMoviePy)
        self.title.setGeometry(QtCore.QRect(50, 0, 441, 101))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.Source = QtWidgets.QPushButton(BeautifulMoviePy)
        self.Source.setGeometry(QtCore.QRect(30, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.Source.setFont(font)
        self.Source.setObjectName("Source")
        self.target = QtWidgets.QPushButton(BeautifulMoviePy)
        self.target.setGeometry(QtCore.QRect(30, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.target.setFont(font)
        self.target.setObjectName("target")
        self.SourcePath = QtWidgets.QTextBrowser(BeautifulMoviePy)
        self.SourcePath.setGeometry(QtCore.QRect(140, 100, 341, 31))
        self.SourcePath.setObjectName("SourcePath")
        self.OutputPath = QtWidgets.QTextBrowser(BeautifulMoviePy)
        self.OutputPath.setGeometry(QtCore.QRect(140, 150, 341, 31))
        self.OutputPath.setObjectName("OutputPath")
        self.startOption = QtWidgets.QCheckBox(BeautifulMoviePy)
        self.startOption.setGeometry(QtCore.QRect(30, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.startOption.setFont(font)
        self.startOption.setObjectName("startOption")
        self.endOption = QtWidgets.QCheckBox(BeautifulMoviePy)
        self.endOption.setGeometry(QtCore.QRect(280, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.endOption.setFont(font)
        self.endOption.setObjectName("endOption")
        self.startTimes = QtWidgets.QTextEdit(BeautifulMoviePy)
        self.startTimes.setGeometry(QtCore.QRect(30, 230, 201, 31))
        self.startTimes.setObjectName("startTimes")
        self.endTimes = QtWidgets.QTextEdit(BeautifulMoviePy)
        self.endTimes.setGeometry(QtCore.QRect(280, 230, 201, 31))
        self.endTimes.setObjectName("endTimes")
        self.fftOption = QtWidgets.QCheckBox(BeautifulMoviePy)
        self.fftOption.setGeometry(QtCore.QRect(30, 280, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.fftOption.setFont(font)
        self.fftOption.setObjectName("fftOption")
        self.IncreaseV = QtWidgets.QCheckBox(BeautifulMoviePy)
        self.IncreaseV.setGeometry(QtCore.QRect(30, 310, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.IncreaseV.setFont(font)
        self.IncreaseV.setObjectName("IncreaseV")
        self.DecreaseV = QtWidgets.QCheckBox(BeautifulMoviePy)
        self.DecreaseV.setGeometry(QtCore.QRect(280, 310, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.DecreaseV.setFont(font)
        self.DecreaseV.setObjectName("DecreaseV")
        self.increaseInput = QtWidgets.QTextEdit(BeautifulMoviePy)
        self.increaseInput.setGeometry(QtCore.QRect(30, 360, 141, 41))
        self.increaseInput.setObjectName("increaseInput")
        self.decreaseInput = QtWidgets.QTextEdit(BeautifulMoviePy)
        self.decreaseInput.setGeometry(QtCore.QRect(280, 360, 141, 41))
        self.decreaseInput.setObjectName("decreaseInput")
        self.label = QtWidgets.QLabel(BeautifulMoviePy)
        self.label.setGeometry(QtCore.QRect(180, 380, 47, 12))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(BeautifulMoviePy)
        self.label_2.setGeometry(QtCore.QRect(430, 380, 47, 12))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.toMP4 = QtWidgets.QPushButton(BeautifulMoviePy)
        self.toMP4.setGeometry(QtCore.QRect(50, 430, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.toMP4.setFont(font)
        self.toMP4.setObjectName("toMP4")
        self.toGIF = QtWidgets.QPushButton(BeautifulMoviePy)
        self.toGIF.setGeometry(QtCore.QRect(270, 430, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.toGIF.setFont(font)
        self.toGIF.setObjectName("toGIF")
        self.status = QtWidgets.QLabel(BeautifulMoviePy)
        self.status.setGeometry(QtCore.QRect(30, 510, 451, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.status.setFont(font)
        self.status.setText("")
        self.status.setObjectName("status")

        self.retranslateUi(BeautifulMoviePy)
        QtCore.QMetaObject.connectSlotsByName(BeautifulMoviePy)

    def retranslateUi(self, BeautifulMoviePy):
        _translate = QtCore.QCoreApplication.translate
        BeautifulMoviePy.setWindowTitle(_translate("BeautifulMoviePy", "BeautifulMoviePy"))
        self.title.setText(_translate("BeautifulMoviePy", "BeautifulMoviePy"))
        self.Source.setText(_translate("BeautifulMoviePy", "Source Path"))
        self.target.setText(_translate("BeautifulMoviePy", "OutputPath"))
        self.startOption.setText(_translate("BeautifulMoviePy", "Start"))
        self.endOption.setText(_translate("BeautifulMoviePy", "End"))
        self.fftOption.setText(_translate("BeautifulMoviePy", "remove silence audio(Beta)"))
        self.IncreaseV.setText(_translate("BeautifulMoviePy", "Increase Volume"))
        self.DecreaseV.setText(_translate("BeautifulMoviePy", "Decrease Volume"))
        self.label.setText(_translate("BeautifulMoviePy", "Times"))
        self.label_2.setText(_translate("BeautifulMoviePy", "Times"))
        self.toMP4.setText(_translate("BeautifulMoviePy", "->mp4"))
        self.toGIF.setText(_translate("BeautifulMoviePy", "->GIF"))

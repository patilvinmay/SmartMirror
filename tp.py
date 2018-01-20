# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebKitWidgets
from PyQt5.QtCore import QUrl

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(680, 30, 120, 551))
        self.groupBox.setStyleSheet("background-color: black; color: white;")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 80, 80))
        self.pushButton.setStyleSheet("background-image: url(\"f.png\");")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 340, 80, 80))
        self.pushButton_4.setStyleSheet("background-image: url(\"f.png\");")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 440, 80, 80))
        self.pushButton_5.setStyleSheet("background-image: url(\"f.png\");")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(60, 80, 431, 411))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 230, 80, 80))
        self.pushButton_2.setStyleSheet("background-image: url(\"f.png\");")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 340, 80, 80))
        self.pushButton_3.setStyleSheet("background-image: url(\"f.png\");")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.direct)
        self.pushButton_2.clicked.connect(self.groupBox.hide)
        self.pushButton_3.clicked.connect(self.groupBox.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def direct(self):
        self.webView.setUrl(QUrl("http://www.youtube.com"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))

from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practise.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtTest
from pygame import mixer
import requests
from PyQt5.QtCore import QUrl
import datetime
from PyQt5.QtWebKit import QWebSettings
from bluetooth import*

class Ui_MainWindow(object):
    flag=1
    flag_2=0
    gp5flag=0
    sa2flag=1
    songno=0
    saflag=1
    allflag=1
    ha15flag=0
    ha12flag=0
    ha13flag=0
    ha14flag=0
    ha16flag=0
    ha18flag=0
    ha19flag=0
    ha20flag=0
    songs= ["a.mp3", "b.mp3", "c.mp3", "d.mp3", "e.mp3", "f.mp3", "g.mp3", "h.mp3", "i.mp3", "j.mp3", "k.mp3", "l.mp3",]


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 1880)
        MainWindow.setStyleSheet("color: white; background-color: black;")
        MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
        mixer.init()
        mixer.music.load("a.mp3")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 40, 311, 151))                                 #groupbox
        self.groupBox.setStyleSheet("color: white; background-color: black; border:0;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setStyleSheet("color: white; background-color: black;")                  #label
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)


        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white; background-color: black;")                   #label2
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)


        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white; background-color: black; border: 0;")            #label3
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(750, 10, 321, 211))
        self.groupBox_3.setStyleSheet("color: white; background-color: black; border:0;")           #groupbox3
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)


        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: white; background-color: black;")                   #label 15
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)


        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: white; background-color: black;")
        self.label_16.setObjectName("label_16")                                                                      #label 16
        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)


        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: white; background-color: black;")                   #label 17
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)


        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: white; background-color: black;")                       #label 18
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 4, 0, 1, 1)


        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: white; background-color: black;")                           #label  19
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 1, 1, 1)


        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: white; background-color: black;")                       #label 20
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 4, 1, 1, 4)


        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setStyleSheet("color: white; background-color: black;")                                           #label 21
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 0, 1, 1, 4)


        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setStyleSheet("color: white; background-color: black;")
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)                     #label 22
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 1, 4, 1, 1)


        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)                                                                                             #label 23
        self.label_23.setStyleSheet("color: white; background-color: black;")
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 1, 1, 4)


        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: white; background-color: black;")                                                   #label_24
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 2, 1, 1, 4)


        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: white; background-color: black;")                                               #label 25
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 1, 2, 1, 1)


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 1800, 450, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)                                                                                               #label  4
        self.label_4.setObjectName("label_4")


        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(940, 1800, 40, 40))
        self.pushButton_7.setStyleSheet("background-image:url(\"w.png\");")                                                     #push button 7
        self.pushButton_7.setText("")
        self.pushButton_7.clicked.connect(self.sa2)
        self.pushButton_7.setObjectName("pushButton_7")


        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(949, 240, 131, 131))
        self.dial.setStyleSheet("color: white; background-color:white;")                                                    # dial
        self.dial.valueChanged.connect(self.vol)
        self.dial.setObjectName("dial")


        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 270, 290, 90))
        self.groupBox_4.setStyleSheet("background-color:black;")                                                                      # group box 4
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")


        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.pushButton_8.setStyleSheet("background-image:url(\"previous.png\")")                                                            #Pushbutton 8
        self.pushButton_8.setText("")
        self.pushButton_8.clicked.connect(self.preSong)
        self.pushButton_8.setObjectName("pushButton_8")


        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 10, 70, 70))
        self.pushButton_9.setStyleSheet("background-image:url(\"play.png\")")                                   # pushbutton 9
        self.pushButton_9.setText("")
        self.pushButton_9.clicked.connect(self.play)
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 10, 70, 70))
        self.pushButton_10.setStyleSheet("background-image:url(\"forward.png\")")                   #push Button 10
        self.pushButton_10.setText("")
        self.pushButton_10.clicked.connect(self.nextSong)
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(985, 1800, 40, 40))
        self.pushButton_17.setStyleSheet("background-image:url(\"home.png\")")                          #push button 17
        self.pushButton_17.setText("")
        self.pushButton_17.clicked.connect(self.hagp)
        self.pushButton_17.setObjectName("pushButton_17")

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(1040, 1800, 40, 40))
        self.pushButton_11.setStyleSheet("color:black; background-color:black; background-image: url(\"soff.png\");")           #pushbutton 11
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.hideall)

        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 1690, 671, 91))
        self.groupBox_5.setStyleSheet("background-color:black; border:0;")              #groupbox 5
        self.groupBox_5.hide()
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")

        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_12.setGeometry(QtCore.QRect(580, 10, 70, 70))
        self.pushButton_12.setStyleSheet("background-image:url(\"off.png\")")                   #pushbutton 12
        self.pushButton_12.setText("")
        self.pushButton_12.clicked.connect(self.twoon)
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_13.setGeometry(QtCore.QRect(340, 10, 70, 70))
        self.pushButton_13.setStyleSheet("background-image:url(\"off.png\")")                    #pushbutton 13
        self.pushButton_13.setText("")
        self.pushButton_13.clicked.connect(self.threeon)
        self.pushButton_13.setObjectName("pushButton_13")

        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_14.setGeometry(QtCore.QRect(100, 10, 70, 70))
        self.pushButton_14.setStyleSheet("background-image:url(\"off.png\")")                        #pushbutton 14
        self.pushButton_14.setText("")
        self.pushButton_14.clicked.connect(self.fouron)
        self.pushButton_14.setObjectName("pushButton_14")

        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_15.setGeometry(QtCore.QRect(20, 10, 70, 70))
        self.pushButton_15.setStyleSheet("background-image:url(\"off.png\")")                            #pushbutton 15
        self.pushButton_15.setText("")
        self.pushButton_15.clicked.connect(self.oneon)
        self.pushButton_15.setObjectName("pushButton_15")

        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_16.setGeometry(QtCore.QRect(420, 10, 70, 70))
        self.pushButton_16.setStyleSheet("background-image:url(\"off.png\")")                            #pushbutton 16
        self.pushButton_16.setText("")
        self.pushButton_16.clicked.connect(self.fiveon)
        self.pushButton_16.setObjectName("pushButton_16")

        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_18.setGeometry(QtCore.QRect(180, 10, 70, 70))
        self.pushButton_18.setStyleSheet("background-image:url(\"off.png\")")                            #pushbutton 18
        self.pushButton_18.setText("")
        self.pushButton_18.clicked.connect(self.sixon)
        self.pushButton_18.setObjectName("pushButton_18")

        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_19.setGeometry(QtCore.QRect(500, 10, 70, 70))
        self.pushButton_19.setStyleSheet("background-image:url(\"off.png\")")                                #pushbutton 19
        self.pushButton_19.setText("")
        self.pushButton_19.clicked.connect(self.sevenon)
        self.pushButton_19.setObjectName("pushButton_19")

        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_20.setGeometry(QtCore.QRect(260, 10, 70, 70))
        self.pushButton_20.setStyleSheet("background-image:url(\"off.png\")")                            #pushbutton 20
        self.pushButton_20.setText("")
        self.pushButton_20.clicked.connect(self.eighton)
        self.pushButton_20.setObjectName("pushButton_20")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 400, 401, 581))
        self.scrollArea.setStyleSheet("background-color:black; color: white;")                  #scroll area
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 382, 948))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_11 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)                       #groupbox 11
        self.groupBox_11.setMinimumSize(QtCore.QSize(360, 150))
        self.groupBox_11.setStyleSheet("border:0;")
        self.groupBox_11.setTitle("")
        self.groupBox_11.setObjectName("groupBox_11")

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_11)
        self.verticalLayout_9.setObjectName("verticalLayout_9")

        self.label_30 = QtWidgets.QLabel(self.groupBox_11)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:white;")
        self.label_30.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_30.setTextFormat(QtCore.Qt.AutoText)                                     #label 30
        self.label_30.setWordWrap(True)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_9.addWidget(self.label_30)

        self.label_31 = QtWidgets.QLabel(self.groupBox_11)
        self.label_31.setStyleSheet("color:white;")                                             #label 31
        self.label_31.setTextFormat(QtCore.Qt.AutoText)
        self.label_31.setWordWrap(True)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_9.addWidget(self.label_31)

        self.gridLayout_2.addWidget(self.groupBox_11, 2, 1, 1, 1)
        self.groupBox_12 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_12.setMinimumSize(QtCore.QSize(360, 150))                            #groupbox 12
        self.groupBox_12.setStyleSheet("border:0;")
        self.groupBox_12.setTitle("")
        self.groupBox_12.setObjectName("groupBox_12")

        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_12)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        self.label_32 = QtWidgets.QLabel(self.groupBox_12)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color:white;")
        self.label_32.setFrameShadow(QtWidgets.QFrame.Plain)                                    #label 32
        self.label_32.setTextFormat(QtCore.Qt.AutoText)
        self.label_32.setWordWrap(True)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_10.addWidget(self.label_32)


        self.label_33 = QtWidgets.QLabel(self.groupBox_12)
        self.label_33.setStyleSheet("color:white;")
        self.label_33.setTextFormat(QtCore.Qt.AutoText)                                     #label 33
        self.label_33.setWordWrap(True)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_10.addWidget(self.label_33)

        self.gridLayout_2.addWidget(self.groupBox_12, 1, 1, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_9.setMinimumSize(QtCore.QSize(360, 150))                          #group box 9
        self.groupBox_9.setStyleSheet("border:0;")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.label_26 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)


        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:white;")
        self.label_26.setFrameShadow(QtWidgets.QFrame.Plain)                                #label 26
        self.label_26.setTextFormat(QtCore.Qt.AutoText)
        self.label_26.setWordWrap(True)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_7.addWidget(self.label_26)

        self.label_27 = QtWidgets.QLabel(self.groupBox_9)
        self.label_27.setStyleSheet("color:white;")
        self.label_27.setTextFormat(QtCore.Qt.AutoText)
        self.label_27.setWordWrap(True)                                                                                 #label 27
        self.label_27.setObjectName("label_27")
        self.verticalLayout_7.addWidget(self.label_27)

        self.gridLayout_2.addWidget(self.groupBox_9, 4, 1, 1, 1)
        self.groupBox_10 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_10.setMinimumSize(QtCore.QSize(360, 150))
        self.groupBox_10.setStyleSheet("border:0;")                                                                     #group box 10
        self.groupBox_10.setTitle("")
        self.groupBox_10.setObjectName("groupBox_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_28 = QtWidgets.QLabel(self.groupBox_10)

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:white;")
        self.label_28.setFrameShadow(QtWidgets.QFrame.Plain)                                        #label 28
        self.label_28.setTextFormat(QtCore.Qt.AutoText)
        self.label_28.setWordWrap(True)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_8.addWidget(self.label_28)


        self.label_29 = QtWidgets.QLabel(self.groupBox_10)
        self.label_29.setStyleSheet("color:white;")
        self.label_29.setTextFormat(QtCore.Qt.AutoText)                                                         #label 28
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_8.addWidget(self.label_29)

        self.gridLayout_2.addWidget(self.groupBox_10, 5, 1, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_8.setMinimumSize(QtCore.QSize(360, 150))
        self.groupBox_8.setStyleSheet("border:0;")                                              #group box 8
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.label_13 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:white;")
        self.label_13.setFrameShadow(QtWidgets.QFrame.Plain)                            #label 13
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)


        self.label_14 = QtWidgets.QLabel(self.groupBox_8)
        self.label_14.setStyleSheet("color:white;")
        self.label_14.setTextFormat(QtCore.Qt.AutoText)                                     #label 14
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)


        self.gridLayout_2.addWidget(self.groupBox_8, 3, 1, 1, 1)
        self.groupBox_13 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_13.setMinimumSize(QtCore.QSize(360, 150))
        self.groupBox_13.setStyleSheet("border:0;")
        self.groupBox_13.setTitle("")                                                           #group box 13
        self.groupBox_13.setObjectName("groupBox_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_13)

        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_34 = QtWidgets.QLabel(self.groupBox_13)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color:white;")                                                                                 #label 34
        self.label_34.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_34.setTextFormat(QtCore.Qt.AutoText)
        self.label_34.setWordWrap(True)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_11.addWidget(self.label_34)


        self.label_35 = QtWidgets.QLabel(self.groupBox_13)
        self.label_35.setStyleSheet("color:white;")
        self.label_35.setTextFormat(QtCore.Qt.AutoText)                                                                                 #label 35
        self.label_35.setWordWrap(True)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_11.addWidget(self.label_35)


        self.gridLayout_2.addWidget(self.groupBox_13, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(977, 400, 121, 955))                             #scroll area2
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 102, 958))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")                                     #scroll area
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.pushButton_25 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_25.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_25.setStyleSheet("color:black; background-color:white; background-image: url(\"t.jpg\");")                  #pushbutton 25
        self.pushButton_25.setText("")
        self.pushButton_25.clicked.connect(self.twitter)
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_4.addWidget(self.pushButton_25, 5, 0, 1, 1)

        self.pushButton_21 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_21.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_21.setStyleSheet("color:black; background-color:white; background-image: url(\"g.png\");")                      #pushbutton 21
        self.pushButton_21.setText("")
        self.pushButton_21.clicked.connect(self.gplus)
        self.pushButton_21.setObjectName("pushButton_21")


        self.gridLayout_4.addWidget(self.pushButton_21, 1, 0, 1, 1)

        self.pushButton_27 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_27.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_27.setStyleSheet("color:black; background-color:white; background-image: url(\"y.jpg\");")                              #pushbutton 27
        self.pushButton_27.setText("")
        self.pushButton_27.clicked.connect(self.youtube)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_4.addWidget(self.pushButton_27, 6, 0, 1, 1)

        self.pushButton_24 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_24.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_24.setStyleSheet("color:black; background-color:white; background-image: url(\"q.png\");")                                  #pushbutton 24
        self.pushButton_24.setText("")
        self.pushButton_24.clicked.connect(self.quora)
        self.pushButton_24.setObjectName("pushButton_24")

        self.gridLayout_4.addWidget(self.pushButton_24, 4, 0, 1, 1)

        self.pushButton_29 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_29.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_29.setStyleSheet("color:black; background-color:white; background-image: url(\"f.png\");")                                  #pushbutton 29
        self.pushButton_29.setText("")
        self.pushButton_29.clicked.connect(self.facebook)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_4.addWidget(self.pushButton_29, 0, 0, 1, 1)


        self.pushButton_22 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_22.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_22.setStyleSheet("color:black; background-color:white; background-image: url(\"gp.png\");")                                 #pushbutton 22
        self.pushButton_22.setText("")
        self.pushButton_22.clicked.connect(self.photos)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_4.addWidget(self.pushButton_22, 8, 0, 1, 1)

        self.pushButton_28 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_28.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_28.setStyleSheet("color:black; background-color:white;background-image: url(\"i.png\");")                               #pushbutton 28
        self.pushButton_28.setText("")
        self.pushButton_28.clicked.connect(self.instagram)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_4.addWidget(self.pushButton_28, 2, 0, 1, 1)

        self.pushButton_26 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_26.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_26.setStyleSheet("color:black; background-color:white; background-image: url(\"l.jpg\");")                                  #pushbutton 19
        self.pushButton_26.setText("")
        self.pushButton_26.clicked.connect(self.linkedin)
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_4.addWidget(self.pushButton_26, 3, 0, 1, 1)

        self.pushButton_23 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_23.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_23.setStyleSheet("color:black; background-color:white; background-image: url(\"m.png\");")                          #pushbutton 23
        self.pushButton_23.setText("")
        self.pushButton_23.clicked.connect(self.gmap)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_4.addWidget(self.pushButton_23, 7, 0, 1, 1)


        self.pushButton_31 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_31.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_31.setStyleSheet("color:black; background-color:white; background-image: url(\"gmail.png\");")                      #pushbutton 31
        self.pushButton_31.setText("")
        self.pushButton_31.clicked.connect(self.gmail)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_4.addWidget(self.pushButton_31, 9, 0, 1, 1)

        self.pushButton_32 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_32.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_32.setStyleSheet("color:black; background-color:white; background-image: url(\"y.png\");")                                  #pushbutton 32
        self.pushButton_32.setText("")
        self.pushButton_32.clicked.connect(self.yahoo)
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_4.addWidget(self.pushButton_32, 10, 0, 1, 1)

        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(840, 1800, 40, 40))                                                     #pushbutton 33
        self.pushButton_33.setStyleSheet("background-image:url(\"bt.png\");")
        self.pushButton_33.setText("")
        #self.pushButton_33.clicked.connect(self.btcon)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.webView = QtWebKitWidgets.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))                                 #webview
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")

        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(890, 1800, 40, 40))
        self.pushButton_30.setStyleSheet("background-image:url(\"gn.png\");")                                               #pushbutton 30
        self.pushButton_30.setText("")
        self.pushButton_30.clicked.connect(self.sa)
        self.pushButton_30.setObjectName("pushButton_30")


        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(1009, 370, 71, 21))                         #lcd no
        self.lcdNumber.setObjectName("lcdNumber")

        self.webView.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.label_4.raise_()
        self.pushButton_7.raise_()
        self.dial.raise_()
        self.groupBox_4.raise_()
        self.pushButton_17.raise_()
        self.pushButton_11.raise_()
        self.groupBox_5.raise_()
        self.scrollArea.raise_()
        self.scrollArea_2.raise_()
        self.pushButton_30.raise_()
        self.lcdNumber.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "24 : 03 : 25"))
        self.label_2.setText(_translate("MainWindow", "Wednesday"))
        self.label_3.setText(_translate("MainWindow", "24 - 12 - 17"))
        self.label_15.setText(_translate("MainWindow", "28.0"))
        self.label_16.setText(_translate("MainWindow", "Wind Speed: "))
        self.label_17.setText(_translate("MainWindow", "Humidity:"))
        self.label_18.setText(_translate("MainWindow", "Air Pressure:"))
        self.label_19.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "1017 Pa"))
        self.label_21.setText(_translate("MainWindow", "Mumbai"))
        self.label_22.setText(_translate("MainWindow", "Smoke"))
        self.label_23.setText(_translate("MainWindow", "20 %"))
        self.label_24.setText(_translate("MainWindow", "50 Km/h"))
        self.label_25.setText(_translate("MainWindow", "C"))
        self.label_4.setText(_translate("MainWindow", "Hello! You are looking amzing!"))
        self.label_30.setText(_translate("MainWindow", "Title Here!!!!!"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p>Description</p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "Title Here!!!!!"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p>Description</p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "Title Here!!!!!"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p>Description</p></body></html>"))
        self.label_28.setText(_translate("MainWindow", "Title Here!!!!!"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p>Description</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "Title Here!!!!!"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>Description</p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "Title Here!!!!!"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p>Description</p></body></html>"))

    def shTime(self):
        a = 0
        while True:
            now = datetime.datetime.now()
            self.label.setText("%d : %d" % (now.hour, now.minute))
            if now.hour>=00 and now.minute>=00 and now.hour<=4 and now.minute<=59:
                self.label_4.setText("Good Night! Time to sleep..")
            elif now.hour >= 5 and now.minute >= 00 and now.hour <= 11 and now.minute <= 59:
                self.label_4.setText("Good Morning ! Ur Looking amazing!")
            elif now.hour >= 12 and now.minute >= 00 and now.hour <= 16 and now.minute <= 59:
                self.label_4.setText("Good Afternoon! Dont Forget to smile")
            elif now.hour >= 17 and now.minute >= 00 and now.hour <= 20 and now.minute <= 59:
                self.label_4.setText("Good Evening! Its Tea Time..")
            elif now.hour >= 21 and now.minute >= 00 and now.hour <= 23 and now.minute <= 59:
                self.label_4.setText("Remember moments of your day")
            a = now.today().weekday()
            if a == 0:
                self.label_2.setText("Monday")
            elif a == 1:
                self.label_2.setText("Tuesday")
            elif a == 2:
                self.label_2.setText("Wednesday")
            elif a == 3:
                self.label_2.setText("Thursday")
            elif a == 4:
                self.label_2.setText("Friday")
            elif a == 5:
                self.label_2.setText("Saturday")
            elif a == 6:
                self.label_2.setText("Sunday")
            self.label_3.setText("%d - %d - %d" % (now.day, now.month, now.year))
            self.upweather()
            self.fill()
            QtTest.QTest.qWait(60000)

    def upweather(self):
        add = "http://api.openweathermap.org/data/2.5/weather?appid=4d0b2138800c289652fe9745834651a6&q="
        city = "Mumbai"
        url = add + city
        data = requests.get(url).json()
        weather = data['weather'][0]['main']
        factor1 = str(int(data['main']['temp']) / 10)
        factor2 = str(data['main']['humidity']) + " %"
        factor3 = str(data['main']['pressure']) + " Pa"
        factor4 = str(data['wind']['speed']) + " Km/h"
        self.label_15.setText(factor1)
        self.label_21.setText(city)
        self.label_24.setText(factor4)
        self.label_23.setText(factor2)
        self.label_20.setText(factor3)
        self.label_22.setText(weather)

    def play(self):
        if self.flag==1:
            self.pushButton_9.setStyleSheet("background-image: url(\"pause.png\")")
            self.flag=0
            if self.flag_2==0:
                mixer.music.play()
            elif self.flag_2==1:
                mixer.music.unpause()
        elif self.flag==0:
            self.pushButton_9.setStyleSheet("background-image: url(\"play.png\")")
            self.flag=1
            self.flag_2=1
            mixer.music.pause()

    def vol(self):
        a=self.dial.value()/100
        mixer.music.set_volume(a)

    def nextSong(self):
        if self.songno<11:
            mixer.music.stop()
            self.songno=self.songno+1
            mixer.music.load(str(self.songs[self.songno]))
            mixer.music.play()
        elif self.songno==11:
            mixer.music.stop()
            self.songno = 0
            mixer.music.load(str(self.songs[self.songno]))
            mixer.music.play()

    def preSong(self):
        if self.songno ==0:
            mixer.music.stop()
            self.songno=11
            mixer.music.load(str(self.songs[self.songno]))
            mixer.music.play()
        elif self.songno>0:
            mixer.music.stop()
            self.songno = self.songno-1
            mixer.music.load(str(self.songs[self.songno]))
            mixer.music.play()

    def fill(self):
        url = ('https://newsapi.org/v2/top-headlines?'
               'sources=the-times-of-india&'
               'apiKey=57f19622826d450289a6b86589e74c31')
        response = requests.get(url).json()
        title = response['articles'][0]['title']
        description = response['articles'][0]['description']
        self.label_34.setText(title)
        self.label_35.setText(description)

        title = response['articles'][1]['title']
        description = response['articles'][1]['description']
        self.label_32.setText(title)
        self.label_33.setText(description)

        title = response['articles'][2]['title']
        description = response['articles'][2]['description']
        self.label_30.setText(title)
        self.label_31.setText(description)

        title = response['articles'][3]['title']
        description = response['articles'][3]['description']
        self.label_13.setText(title)
        self.label_14.setText(description)

        title = response['articles'][4]['title']
        description = response['articles'][4]['description']
        self.label_28.setText(title)
        self.label_29.setText(description)

        title = response['articles'][5]['title']
        description = response['articles'][5]['description']
        self.label_26.setText(title)
        self.label_27.setText(description)

    def hagp(self):
        if self.gp5flag==1:
            self.groupBox_5.hide()
            self.gp5flag=0
        elif self.gp5flag==0:
            self.groupBox_5.show()
            self.gp5flag=1

    def sa2(self):
        if self.sa2flag==1:
            self.scrollArea_2.hide()
            self.sa2flag=0
        elif self.sa2flag==0:
            self.scrollArea_2.show()
            self.sa2flag=1

    def sa(self):
        if self.saflag==1:
            self.scrollArea.hide()
            self.saflag=0
        elif self.saflag==0:
            self.scrollArea.show()
            self.saflag=1

    def hideall(self):
        if self.allflag==1:
            self.pushButton_11.setStyleSheet("background-image: url(\"son.png\")")
            self.groupBox_4.hide()
            self.dial.hide()
            self.lcdNumber.hide()
            self.scrollArea_2.hide()
            self.webView.hide()
            self.scrollArea.hide()
            self.pushButton_30.hide()
            self.pushButton_17.hide()
            self.pushButton_7.hide()
            self.groupBox_5.hide()
            self.sa2flag = 0
            self.saflag = 0
            self.gp5flag = 0
            self.allflag=0
        elif self.allflag==0:
            self.pushButton_11.setStyleSheet("background-image: url(\"soff.png\")")
            self.groupBox_4.show()
            self.dial.show()
            self.lcdNumber.show()
            self.scrollArea_2.show()
            self.webView.show()
            self.scrollArea.show()
            self.pushButton_30.show()
            self.pushButton_17.show()
            self.pushButton_7.show()
            self.groupBox_5.show()
            self.sa2flag=1
            self.saflag=1
            self.gp5flag=1
            self.allflag=1

    def oneon(self):
        if self.ha15flag==0:
            self.pushButton_15.setStyleSheet("background-image: url(\"on.png\")")
            self.ha15flag=1
        elif self.ha15flag==1:
            self.pushButton_15.setStyleSheet("background-image: url(\"off.png\")")
            self.ha15flag=0

    def twoon(self):
        if self.ha12flag==0:
            self.pushButton_12.setStyleSheet("background-image: url(\"on.png\")")
            self.ha12flag=1
        elif self.ha12flag==1:
            self.pushButton_12.setStyleSheet("background-image: url(\"off.png\")")
            self.ha12flag=0

    def threeon(self):
        if self.ha13flag==0:
            self.pushButton_13.setStyleSheet("background-image: url(\"on.png\")")
            self.ha13flag=1
        elif self.ha13flag==1:
            self.pushButton_13.setStyleSheet("background-image: url(\"off.png\")")
            self.ha13flag=0

    def fouron(self):
        if self.ha14flag==0:
            self.pushButton_14.setStyleSheet("background-image: url(\"on.png\")")
            self.ha14flag=1
        elif self.ha14flag==1:
            self.pushButton_14.setStyleSheet("background-image: url(\"off.png\")")
            self.ha14flag=0

    def fiveon(self):
        if self.ha16flag==0:
            self.pushButton_16.setStyleSheet("background-image: url(\"on.png\")")
            self.ha16flag=1
        elif self.ha16flag==1:
            self.pushButton_16.setStyleSheet("background-image: url(\"off.png\")")
            self.ha16flag=0


    def sixon(self):
        if self.ha18flag==0:
            self.pushButton_18.setStyleSheet("background-image: url(\"on.png\")")
            self.ha18flag=1
        elif self.ha18flag==1:
            self.pushButton_18.setStyleSheet("background-image: url(\"off.png\")")
            self.ha18flag=0

    def sevenon(self):
        if self.ha19flag==0:
            self.pushButton_19.setStyleSheet("background-image: url(\"on.png\")")
            self.ha19flag=1
        elif self.ha19flag==1:
            self.pushButton_19.setStyleSheet("background-image: url(\"off.png\")")
            self.ha19flag=0

    def eighton(self):
        if self.ha20flag==0:
            self.pushButton_20.setStyleSheet("background-image: url(\"on.png\")")
            self.ha20flag=1
        elif self.ha20flag==1:
            self.pushButton_20.setStyleSheet("background-image: url(\"off.png\")")
            self.ha20flag=0


    def facebook(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://www.facebook.com"))

    def gplus(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://www.google.com"))

    def instagram(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://www.instagram.com"))

    def linkedin(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://www.linkedin.com"))

    def quora(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://www.quora.com"))

    def twitter(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://www.twitter.com"))

    def youtube(self):
        self.webView.setGeometry(QtCore.QRect(490, 1000, 468, 640))
        self.webView.setUrl(QUrl("http://www.youtube.com"))

    def gmap(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://maps.google.com"))

    def photos(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://www.outlook.com"))

    def gmail(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://mail.google.com"))

    def yahoo(self):
        self.webView.setGeometry(QtCore.QRect(126, 1140, 840, 520))
        self.webView.setUrl(QUrl("http://www.yahoo.com"))








from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.shTime()
    sys.exit(app.exec_())


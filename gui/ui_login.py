# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(20, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblUsername = QtWidgets.QLabel(self.centralwidget)
        self.lblUsername.setGeometry(QtCore.QRect(70, 80, 121, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblUsername.setFont(font)
        self.lblUsername.setObjectName("lblUsername")
        self.lblPassword = QtWidgets.QLabel(self.centralwidget)
        self.lblPassword.setGeometry(QtCore.QRect(70, 130, 131, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.ledtUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtUsername.setGeometry(QtCore.QRect(180, 80, 191, 32))
        self.ledtUsername.setObjectName("ledtUsername")
        self.ledtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.ledtPassword.setGeometry(QtCore.QRect(180, 130, 191, 32))
        self.ledtPassword.setObjectName("ledtPassword")
        self.btnSignIn = QtWidgets.QPushButton(self.centralwidget)
        self.btnSignIn.setGeometry(QtCore.QRect(400, 80, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.btnSignIn.setFont(font)
        self.btnSignIn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSignIn.setObjectName("btnSignIn")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(400, 190, 111, 34))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnExit.setObjectName("btnExit")
        self.lblLoginStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblLoginStatus.setGeometry(QtCore.QRect(180, 180, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblLoginStatus.setFont(font)
        self.lblLoginStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblLoginStatus.setObjectName("lblLoginStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitle.setText(_translate("MainWindow", "Please login to continue..."))
        self.lblUsername.setText(_translate("MainWindow", "Username"))
        self.lblPassword.setText(_translate("MainWindow", "Password"))
        self.btnSignIn.setText(_translate("MainWindow", "Sign in"))
        self.btnExit.setText(_translate("MainWindow", "EXIT"))
        self.lblLoginStatus.setText(_translate("MainWindow", "TextLabel"))


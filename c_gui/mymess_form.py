# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyMessForm.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(831, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 160, 261, 181))
        self.groupBox.setObjectName("groupBox")
        self.listWidgetContants = QtWidgets.QListWidget(self.groupBox)
        self.listWidgetContants.setGeometry(QtCore.QRect(10, 60, 241, 111))
        self.listWidgetContants.setObjectName("listWidgetContants")
        self.lineEditAddContact = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditAddContact.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.lineEditAddContact.setObjectName("lineEditAddContact")
        self.pushAdd = QtWidgets.QPushButton(self.groupBox)
        self.pushAdd.setGeometry(QtCore.QRect(160, 20, 41, 31))
        self.pushAdd.setObjectName("pushAdd")
        self.pushDel = QtWidgets.QPushButton(self.groupBox)
        self.pushDel.setGeometry(QtCore.QRect(210, 20, 41, 31))
        self.pushDel.setObjectName("pushDel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(280, 0, 541, 341))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textAddMessage = QtWidgets.QTextEdit(self.groupBox_2)
        self.textAddMessage.setGeometry(QtCore.QRect(10, 290, 461, 41))
        self.textAddMessage.setOverwriteMode(True)
        self.textAddMessage.setObjectName("textAddMessage")
        self.pushSend = QtWidgets.QPushButton(self.groupBox_2)
        self.pushSend.setGeometry(QtCore.QRect(480, 290, 51, 41))
        self.pushSend.setObjectName("pushSend")
        self.textBrowserMessage = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowserMessage.setGeometry(QtCore.QRect(10, 20, 521, 231))
        self.textBrowserMessage.setOverwriteMode(True)
        self.textBrowserMessage.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textBrowserMessage.setObjectName("textBrowserMessage")
        self.pushBold = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBold.setGeometry(QtCore.QRect(10, 260, 31, 23))
        self.pushBold.setObjectName("pushBold")
        self.pushItalic = QtWidgets.QPushButton(self.groupBox_2)
        self.pushItalic.setGeometry(QtCore.QRect(50, 260, 31, 23))
        self.pushItalic.setObjectName("pushItalic")
        self.pushUnderline = QtWidgets.QPushButton(self.groupBox_2)
        self.pushUnderline.setGeometry(QtCore.QRect(90, 260, 31, 23))
        self.pushUnderline.setObjectName("pushUnderline")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 261, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushAvatar = QtWidgets.QPushButton(self.groupBox_3)
        self.pushAvatar.setGeometry(QtCore.QRect(160, 20, 91, 31))
        self.pushAvatar.setObjectName("pushAvatar")
        self.labelAvatar = QtWidgets.QLabel(self.groupBox_3)
        self.labelAvatar.setGeometry(QtCore.QRect(10, 20, 141, 121))
        self.labelAvatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelAvatar.setLineWidth(1)
        self.labelAvatar.setText("")
        self.labelAvatar.setScaledContents(False)
        self.labelAvatar.setOpenExternalLinks(False)
        self.labelAvatar.setObjectName("labelAvatar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_options = QtWidgets.QAction(MainWindow)
        self.action_options.setObjectName("action_options")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_list_contact = QtWidgets.QAction(MainWindow)
        self.action_list_contact.setObjectName("action_list_contact")
        self.menu.addAction(self.action_list_contact)
        self.menu.addAction(self.action_options)
        self.menu.addAction(self.action_about)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Контакты"))
        self.pushAdd.setText(_translate("MainWindow", "+"))
        self.pushDel.setText(_translate("MainWindow", "-"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Чат"))
        self.textAddMessage.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushSend.setText(_translate("MainWindow", "Send"))
        self.textBrowserMessage.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushBold.setText(_translate("MainWindow", "B"))
        self.pushItalic.setText(_translate("MainWindow", "I"))
        self.pushUnderline.setText(_translate("MainWindow", "U"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Аватар"))
        self.pushAvatar.setText(_translate("MainWindow", "Загрузить"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action_options.setText(_translate("MainWindow", "Настройки"))
        self.action_about.setText(_translate("MainWindow", "О программе"))
        self.action_list_contact.setText(_translate("MainWindow", "Контакты"))


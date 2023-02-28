import sys
import sqlite3

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QSlider, QVBoxLayout, QInputDialog, QColorDialog

from datetime import datetime, timedelta

class Login_design(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 950)
        MainWindow.setMinimumSize(QtCore.QSize(700, 950))
        MainWindow.setMaximumSize(QtCore.QSize(700, 950))
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_log = QtWidgets.QPushButton(self.centralwidget)
        self.btn_log.setGeometry(QtCore.QRect(50, 770, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.btn_log.setFont(font)
        self.btn_log.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(100, 200, 255);\n"
"    border-color: rgb(0, 255, 255);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"")
        self.btn_log.setObjectName("btn_log")
        self.btn_reg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reg.setGeometry(QtCore.QRect(390, 770, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.btn_reg.setFont(font)
        self.btn_reg.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(100, 200, 255);\n"
"    border-color: rgb(0, 255, 255);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.btn_reg.setObjectName("btn_reg")
        self.lb_log = QtWidgets.QLabel(self.centralwidget)
        self.lb_log.setGeometry(QtCore.QRect(240, 210, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lb_log.setFont(font)
        self.lb_log.setStyleSheet("color: rgb(255, 255, 255)")
        self.lb_log.setObjectName("lb_log")
        self.le_email = QtWidgets.QLineEdit(self.centralwidget)
        self.le_email.setGeometry(QtCore.QRect(110, 440, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.le_email.setFont(font)
        self.le_email.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(50, 50, 50);\n"
"}")
        self.le_email.setText("")
        self.le_email.setObjectName("le_email")
        self.le_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.le_pass.setGeometry(QtCore.QRect(110, 550, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.le_pass.setFont(font)
        self.le_pass.setStyleSheet("color: rgb(255, 255, 255);")
        self.le_pass.setText("")
        self.le_pass.setObjectName("le_pass")
        self.lb_email = QtWidgets.QLabel(self.centralwidget)
        self.lb_email.setGeometry(QtCore.QRect(30, 450, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lb_email.setFont(font)
        self.lb_email.setStyleSheet("color:rgb(255, 255, 255)")
        self.lb_email.setObjectName("lb_email")
        self.lb_pass = QtWidgets.QLabel(self.centralwidget)
        self.lb_pass.setGeometry(QtCore.QRect(30, 560, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.lb_pass.setFont(font)
        self.lb_pass.setStyleSheet("color: rgb(255, 255, 255)")
        self.lb_pass.setObjectName("lb_pass")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(40, 820, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setStrikeOut(False)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(100, 200, 255);\n"
"    border-color: rgb(0, 255, 255);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(30, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: none")
        self.btn_back.setObjectName("btn_back")
        self.lb_reg = QtWidgets.QLabel(self.centralwidget)
        self.lb_reg.setGeometry(QtCore.QRect(250, 210, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lb_reg.setFont(font)
        self.lb_reg.setStyleSheet("color: rgb(255, 255, 255)")
        self.lb_reg.setObjectName("lb_reg")
        self.btn_register = QtWidgets.QPushButton(self.centralwidget)
        self.btn_register.setGeometry(QtCore.QRect(40, 820, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setStrikeOut(False)
        self.btn_register.setFont(font)
        self.btn_register.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(100, 200, 255);\n"
"    border-color: rgb(0, 255, 255);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.btn_register.setObjectName("btn_register")
        self.extra_label_pass = QtWidgets.QLabel(self.centralwidget)
        self.extra_label_pass.setGeometry(QtCore.QRect(110, 610, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.extra_label_pass.setFont(font)
        self.extra_label_pass.setStyleSheet("color: rgb(170, 0, 0);")
        self.extra_label_pass.setText("")
        self.extra_label_pass.setObjectName("extra_label_pass")
        self.extra_label_email = QtWidgets.QLabel(self.centralwidget)
        self.extra_label_email.setGeometry(QtCore.QRect(110, 500, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.extra_label_email.setFont(font)
        self.extra_label_email.setStyleSheet("color: rgb(170, 0, 0);")
        self.extra_label_email.setText("")
        self.extra_label_email.setObjectName("extra_label_email")
        self.motivation_speech = QtWidgets.QTextBrowser(self.centralwidget)
        self.motivation_speech.setGeometry(QtCore.QRect(80, 420, 521, 161))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        self.motivation_speech.setFont(font)
        self.motivation_speech.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-width: 0px")
        self.motivation_speech.setObjectName("motivation_speech")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
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
        self.btn_log.setText(_translate("MainWindow", "Войти"))
        self.btn_reg.setText(_translate("MainWindow", "Регистрация"))
        self.lb_log.setText(_translate("MainWindow", "Вход в аккаунт"))
        self.lb_email.setText(_translate("MainWindow", "E-Mail"))
        self.lb_pass.setText(_translate("MainWindow", "Пароль"))
        self.btn_login.setText(_translate("MainWindow", "Войти"))
        self.btn_back.setText(_translate("MainWindow", "<-"))
        self.lb_reg.setText(_translate("MainWindow", "Регистрация"))
        self.btn_register.setText(_translate("MainWindow", "Регистрация"))
        self.motivation_speech.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Impact\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Тренируйся с теми, кто сильнее.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Не сдавайся там, где сдаются другие.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">И победишь там, где победить нельзя</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


class MainPage_design(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 950)
        MainWindow.setMinimumSize(QtCore.QSize(700, 950))
        MainWindow.setMaximumSize(QtCore.QSize(700, 950))
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#main workout
        self.image_strong_man = QtWidgets.QLabel(self.centralwidget)
        self.image_strong_man.setGeometry(QtCore.QRect(-50, 50, 800, 800))
        self.image_strong_man.setText("dberh")
        self.image_strong_man.setObjectName("image_strong_man")
        self.help_lbl = QtWidgets.QLabel(self.centralwidget)
        self.help_lbl.setGeometry(QtCore.QRect(-50, 50, 800, 800))
        self.help_lbl.setText("")
        self.help_lbl.setObjectName("image_strong_man")
        self.help_lbl.setStyleSheet('background-color: rgba(50, 50, 50, 180)')
        self.image_water = QtWidgets.QLabel(self.centralwidget)
        self.image_water.setGeometry(QtCore.QRect(53, 870, 32, 32))
        self.image_water.setText("")
        self.image_water.setObjectName("image_water")
        self.image_d = QtWidgets.QLabel(self.centralwidget)
        self.image_d.setGeometry(QtCore.QRect(193, 870, 32, 32))
        self.image_d.setText("")
        self.image_d.setObjectName("image_d")
        self.image_u = QtWidgets.QLabel(self.centralwidget)
        self.image_u.setGeometry(QtCore.QRect(613, 870, 32, 32))
        self.image_u.setText("")
        self.image_u.setObjectName("image_u")
        self.image_s = QtWidgets.QLabel(self.centralwidget)
        self.image_s.setGeometry(QtCore.QRect(473, 870, 32, 32))
        self.image_s.setText("")
        self.image_s.setObjectName("image_s")
        self.image_work = QtWidgets.QLabel(self.centralwidget)
        self.image_work.setGeometry(QtCore.QRect(333, 870, 32, 32))
        self.image_work.setText("")
        self.image_work.setObjectName("image_work")
        self.btn_water = QtWidgets.QPushButton(self.centralwidget)
        self.btn_water.setGeometry(QtCore.QRect(-1, 850, 140, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_water.setFont(font)
        self.btn_water.setStyleSheet("QPushButton {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgba(50, 50, 50, 0);\n"
                                     "    border-width: 0px;\n"
                                     "    \n"
                                     "    border-style: outset;\n"
                                     "    border-color: rgb(100, 200, 255);\n"
                                     "    border-color: rgb(0, 255, 255);\n"
                                     "    padding-top: 55px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: rgba(111, 111, 111, 50)\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    border-width: 2px\n"
                                     "}")
        self.btn_water.setObjectName("btn_water")
        self.btn_d = QtWidgets.QPushButton(self.centralwidget)
        self.btn_d.setGeometry(QtCore.QRect(140, 850, 140, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_d.setFont(font)
        self.btn_d.setStyleSheet("QPushButton {\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgba(50, 50, 50, 0);\n"
                                 "    border-width: 0px;\n"
                                 "    \n"
                                 "    border-style: outset;\n"
                                 "    border-color: rgb(100, 200, 255);\n"
                                 "    border-color: rgb(0, 255, 255);\n"
                                 "    padding-top: 55px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: rgba(111, 111, 111, 50)\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    border-width: 2px\n"
                                 "}")
        self.btn_d.setObjectName("btn_d")
        self.btn_u = QtWidgets.QPushButton(self.centralwidget)
        self.btn_u.setGeometry(QtCore.QRect(560, 850, 140, 100))
        self.btn_u.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_u.setMaximumSize(QtCore.QSize(700, 950))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_u.setFont(font)
        self.btn_u.setStyleSheet("QPushButton {\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgba(50, 50, 50, 0);\n"
                                 "    border-width: 0px;\n"
                                 "    \n"
                                 "    border-style: outset;\n"
                                 "    border-color: rgb(100, 200, 255);\n"
                                 "    border-color: rgb(0, 255, 255);\n"
                                 "    padding-top: 55px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: rgba(111, 111, 111, 50)\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    border-width: 2px\n"
                                 "}")
        self.btn_u.setObjectName("btn_u")
        self.btn_s = QtWidgets.QPushButton(self.centralwidget)
        self.btn_s.setGeometry(QtCore.QRect(280, 850, 140, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_s.setFont(font)
        self.btn_s.setStyleSheet("QPushButton {\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgba(50, 50, 50, 0);\n"
                                 "    border-width: 0px;\n"
                                 "    \n"
                                 "    border-style: outset;\n"
                                 "    border-color: rgb(100, 200, 255);\n"
                                 "    border-color: rgb(0, 255, 255);\n"
                                 "    padding-top: 55px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: rgba(111, 111, 111, 50)\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    border-width: 2px\n"
                                 "}")
        self.btn_s.setObjectName("btn_s")
        self.btn_work = QtWidgets.QPushButton(self.centralwidget)
        self.btn_work.setGeometry(QtCore.QRect(420, 850, 140, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_work.setFont(font)
        self.btn_work.setStyleSheet("QPushButton {\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    background-color: rgba(50, 50, 50, 0);\n"
                                    "    border-width: 0px;\n"
                                    "    \n"
                                    "    border-style: outset;\n"
                                    "    border-color: rgb(100, 200, 255);\n"
                                    "    border-color: rgb(0, 255, 255);\n"
                                    "    padding-top: 55px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: rgba(111, 111, 111, 50)\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    border-width: 2px\n"
                                    "}")
        self.btn_work.setObjectName("btn_work")
        self.btn_workoutprogram = QtWidgets.QPushButton(self.centralwidget)
        self.btn_workoutprogram.setGeometry(QtCore.QRect(50, 60, 601, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_workoutprogram.setFont(font)
        self.btn_workoutprogram.setStyleSheet("QPushButton {\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    background-color: rgb(50, 50, 50);\n"
                                              "    border-style: outset;\n"
                                              "    border-width: 3px;\n"
                                              "    border-radius: 10px;\n"
                                              "    border-color: rgb(100, 200, 255);\n"
                                              "    border-color: rgb(0, 255, 255);\n"
                                              "    min-width: 10em;\n"
                                              "    padding: 6px;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "  background-color: rgb(100, 200, 255);\n"
                                              "  background-color: rgb(0, 255, 255);\n"
                                              "}")
        self.btn_workoutprogram.setObjectName("btn_workoutprogram")
        self.worklearn_lbl = QtWidgets.QLabel(self.centralwidget)
        self.worklearn_lbl.setGeometry(QtCore.QRect(200, 460, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.worklearn_lbl.setFont(font)
        self.worklearn_lbl.setStyleSheet("color: rgb(255, 255, 255);"
                                         "background-color: rgba(1, 1, 1, 0)")
        self.worklearn_lbl.setObjectName("worklearn_lbl")
        self.btn_power = QtWidgets.QPushButton(self.centralwidget)
        self.btn_power.setGeometry(QtCore.QRect(40, 520, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_power.setFont(font)
        self.btn_power.setStyleSheet("QPushButton {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(50, 50, 50);\n"
                                     "    border-style: outset;\n"
                                     "    border-width: 3px;\n"
                                     "    border-radius: 10px;\n"
                                     "    border-color: rgb(100, 200, 255);\n"
                                     "    border-color: rgb(0, 255, 255);\n"
                                     "    min-width: 10em;\n"
                                     "    padding: 6px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "  background-color: rgb(100, 200, 255);\n"
                                     "  background-color: rgb(0, 255, 255);\n"
                                     "}")
        self.btn_power.setObjectName("btn_power")
        self.btn_vynosliv = QtWidgets.QPushButton(self.centralwidget)
        self.btn_vynosliv.setGeometry(QtCore.QRect(40, 590, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_vynosliv.setFont(font)
        self.btn_vynosliv.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(50, 50, 50);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 3px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: rgb(100, 200, 255);\n"
                                        "    border-color: rgb(0, 255, 255);\n"
                                        "    min-width: 10em;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "  background-color: rgb(100, 200, 255);\n"
                                        "  background-color: rgb(0, 255, 255);\n"
                                        "}")
        self.btn_vynosliv.setObjectName("btn_vynosliv")
        self.btn_massa = QtWidgets.QPushButton(self.centralwidget)
        self.btn_massa.setGeometry(QtCore.QRect(40, 660, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_massa.setFont(font)
        self.btn_massa.setStyleSheet("QPushButton {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(50, 50, 50);\n"
                                     "    border-style: outset;\n"
                                     "    border-width: 3px;\n"
                                     "    border-radius: 10px;\n"
                                     "    border-color: rgb(100, 200, 255);\n"
                                     "    border-color: rgb(0, 255, 255);\n"
                                     "    min-width: 10em;\n"
                                     "    padding: 6px;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "  background-color: rgb(100, 200, 255);\n"
                                     "  background-color: rgb(0, 255, 255);\n"
                                     "}")
        self.btn_massa.setObjectName("btn_massa")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-20, 240, 620, 191))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

# creating_program
        self.metod_lbl = QtWidgets.QLabel(self.centralwidget)
        self.metod_lbl.setGeometry(QtCore.QRect(210, 30, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        self.metod_lbl.setFont(font)
        self.metod_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.metod_lbl.setObjectName("metod_lbl")
        self.count_lbl = QtWidgets.QLabel(self.centralwidget)
        self.count_lbl.setGeometry(QtCore.QRect(220, 150, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        self.count_lbl.setFont(font)
        self.count_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.count_lbl.setObjectName("count_lbl")
        self.btn_creating_pr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_creating_pr.setGeometry(QtCore.QRect(180, 320, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_creating_pr.setFont(font)
        self.btn_creating_pr.setStyleSheet("QPushButton {\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgb(50, 50, 50);\n"
                                           "    border-style: outset;\n"
                                           "    border-width: 3px;\n"
                                           "    border-radius: 10px;\n"
                                           "    border-color: rgb(100, 200, 255);\n"
                                           "    border-color: rgb(0, 255, 255);\n"
                                           "    min-width: 10em;\n"
                                           "    padding: 6px;\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:hover {\n"
                                           "  background-color: rgb(100, 200, 255);\n"
                                           "  background-color: rgb(0, 255, 255);\n"
                                           "}")
        self.btn_creating_pr.setObjectName("btn_creating_pr")
        self.count_of_work = QtWidgets.QComboBox(self.centralwidget)
        self.count_of_work.setGeometry(QtCore.QRect(250, 210, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.count_of_work.setFont(font)
        self.count_of_work.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "alternate-background-color: rgb(50, 50, 50);")
        self.count_of_work.setObjectName("count_of_work")
        self.count_of_work.addItem("")
        self.count_of_work.addItem("")
        self.antog_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.antog_rb.setGeometry(QtCore.QRect(50, 90, 296, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.antog_rb.setFont(font)
        self.antog_rb.setStyleSheet("color: rgb(255, 255, 255);")
        self.antog_rb.setObjectName("antog_rb")
        self.sinerg_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.sinerg_rb.setGeometry(QtCore.QRect(360, 90, 599, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.sinerg_rb.setFont(font)
        self.sinerg_rb.setStyleSheet("color: rgb(255, 255, 255);")
        self.sinerg_rb.setObjectName("sinerg_rb")
        self.btn_backtomainwork = QtWidgets.QPushButton(self.centralwidget)
        self.btn_backtomainwork.setGeometry(QtCore.QRect(20, 30, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_backtomainwork.setFont(font)
        self.btn_backtomainwork.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "border: none")
        self.btn_backtomainwork.setObjectName("btn_backtomainwork")
        self.day1 = QtWidgets.QPushButton(self.centralwidget)
        self.day1.setGeometry(QtCore.QRect(40, 420, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.day1.setFont(font)
        self.day1.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(50, 50, 50);\n"
                                "    border-style: outset;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color: rgb(98, 98, 98);\n"
                                "    min-width: 10em;\n"
                                "    padding: 6px;\n"
                                "}")
        self.day1.setText("")
        self.day1.setObjectName("day1")
        self.day2 = QtWidgets.QPushButton(self.centralwidget)
        self.day2.setGeometry(QtCore.QRect(40, 490, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.day2.setFont(font)
        self.day2.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(50, 50, 50);\n"
                                "    border-style: outset;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color: rgb(98, 98, 98);\n"
                                "    min-width: 10em;\n"
                                "    padding: 6px;\n"
                                "}")
        self.day2.setText("")
        self.day2.setObjectName("day2")
        self.day3 = QtWidgets.QPushButton(self.centralwidget)
        self.day3.setGeometry(QtCore.QRect(40, 560, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.day3.setFont(font)
        self.day3.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(50, 50, 50);\n"
                                "    border-style: outset;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color: rgb(98, 98, 98);\n"
                                "    min-width: 10em;\n"
                                "    padding: 6px;\n"
                                "}")
        self.day3.setText("")
        self.day3.setObjectName("day3")
        self.day4 = QtWidgets.QPushButton(self.centralwidget)
        self.day4.setGeometry(QtCore.QRect(40, 630, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.day4.setFont(font)
        self.day4.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(50, 50, 50);\n"
                                "    border-style: outset;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color: rgb(98, 98, 98);\n"
                                "    min-width: 10em;\n"
                                "    padding: 6px;\n"
                                "}")
        self.day4.setText("")
        self.day4.setObjectName("day4")
        self.day5 = QtWidgets.QPushButton(self.centralwidget)
        self.day5.setGeometry(QtCore.QRect(40, 840, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.day5.setFont(font)
        self.day5.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(50, 50, 50);\n"
                                "    border-style: outset;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color: rgb(98, 98, 98);\n"
                                "    min-width: 10em;\n"
                                "    padding: 6px;\n"
                                "}")
        self.day5.setText("")
        self.day5.setObjectName("day5")
        self.day6 = QtWidgets.QPushButton(self.centralwidget)
        self.day6.setGeometry(QtCore.QRect(40, 770, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.day6.setFont(font)
        self.day6.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(50, 50, 50);\n"
                                "    border-style: outset;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color: rgb(98, 98, 98);\n"
                                "    min-width: 10em;\n"
                                "    padding: 6px;\n"
                                "}")
        self.day6.setText("")
        self.day6.setObjectName("day6")
        self.day7 = QtWidgets.QPushButton(self.centralwidget)
        self.day7.setGeometry(QtCore.QRect(40, 700, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.day7.setFont(font)
        self.day7.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(50, 50, 50);\n"
                                "    border-style: outset;\n"
                                "    border-width: 1px;\n"
                                "    border-radius: 10px;\n"
                                "    border-color: rgb(98, 98, 98);\n"
                                "    min-width: 10em;\n"
                                "    padding: 6px;\n"
                                "}")
        self.day7.setText("")
        self.day7.setObjectName("day7")

# endurance_page
        self.endurance_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.endurance_info.setGeometry(QtCore.QRect(20, 70, 311, 501))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.endurance_info.setFont(font)
        self.endurance_info.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "border: none")
        self.endurance_info.setObjectName("endurance_info")
        self.endurance_img = QtWidgets.QLabel(self.centralwidget)
        self.endurance_img.setGeometry(QtCore.QRect(300, 75, 450, 450))
        self.endurance_img.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.endurance_img.setText("")
        self.endurance_img.setObjectName("endurance_img")
        self.backfromendurance = QtWidgets.QPushButton(self.centralwidget)
        self.backfromendurance.setGeometry(QtCore.QRect(10, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backfromendurance.setFont(font)
        self.backfromendurance.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "border: none")
        self.backfromendurance.setObjectName("backfromendurance")
        self.workonendurance = QtWidgets.QTextBrowser(self.centralwidget)
        self.workonendurance.setGeometry(QtCore.QRect(20, 621, 661, 231))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.workonendurance.setFont(font)
        self.workonendurance.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "border-width: 5px;\n"
                                           "border-color: rgb(170, 0, 0);")
        self.workonendurance.setObjectName("workonendurance")
        self.endurance_name = QtWidgets.QLabel(self.centralwidget)
        self.endurance_name.setGeometry(QtCore.QRect(210, 10, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.endurance_name.setFont(font)
        self.endurance_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.endurance_name.setObjectName("endurance_name")
        MainWindow.setCentralWidget(self.centralwidget)

# power page
        self.power_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.power_info.setGeometry(QtCore.QRect(20, 90, 351, 491))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.power_info.setFont(font)
        self.power_info.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border: none")
        self.power_info.setObjectName("power_info")
        self.power_name = QtWidgets.QLabel(self.centralwidget)
        self.power_name.setGeometry(QtCore.QRect(270, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.power_name.setFont(font)
        self.power_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.power_name.setObjectName("power_name")
        self.power_img = QtWidgets.QLabel(self.centralwidget)
        self.power_img.setGeometry(QtCore.QRect(300, 80, 450, 450))
        self.power_img.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.power_img.setText("")
        self.power_img.setObjectName("power_img")
        self.workonpower = QtWidgets.QTextBrowser(self.centralwidget)
        self.workonpower.setGeometry(QtCore.QRect(20, 620, 661, 211))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.workonpower.setFont(font)
        self.workonpower.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "border-width: 5px;\n"
                                       "border-color: rgb(170, 0, 0);")
        self.workonpower.setObjectName("workonpower")
        self.backfrompower = QtWidgets.QPushButton(self.centralwidget)
        self.backfrompower.setGeometry(QtCore.QRect(10, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backfrompower.setFont(font)
        self.backfrompower.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "border: none")
        self.backfrompower.setObjectName("backfrompower")
        MainWindow.setCentralWidget(self.centralwidget)

# massa page
        self.backfrommassa = QtWidgets.QPushButton(self.centralwidget)
        self.backfrommassa.setGeometry(QtCore.QRect(30, 30, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backfrommassa.setFont(font)
        self.backfrommassa.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "border: none")
        self.backfrommassa.setObjectName("backfrommassa")
        self.massa_name = QtWidgets.QLabel(self.centralwidget)
        self.massa_name.setGeometry(QtCore.QRect(220, 30, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.massa_name.setFont(font)
        self.massa_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.massa_name.setObjectName("massa_name")
        self.massa_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.massa_info.setGeometry(QtCore.QRect(30, 100, 351, 471))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.massa_info.setFont(font)
        self.massa_info.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border: none")
        self.massa_info.setObjectName("massa_info")
        self.workonmassa = QtWidgets.QTextBrowser(self.centralwidget)
        self.workonmassa.setGeometry(QtCore.QRect(20, 610, 661, 221))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.workonmassa.setFont(font)
        self.workonmassa.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "border-width: 5px;\n"
                                       "border-color: rgb(170, 0, 0);")
        self.workonmassa.setObjectName("workonmassa")
        self.massa_img = QtWidgets.QLabel(self.centralwidget)
        self.massa_img.setGeometry(QtCore.QRect(365, 100, 350, 450))
        self.massa_img.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.massa_img.setText("")
        self.massa_img.setObjectName("massa_img")
        MainWindow.setCentralWidget(self.centralwidget)
# water page
        self.weight_slider = QtWidgets.QSlider(self.centralwidget)
        self.weight_slider.setGeometry(QtCore.QRect(30, 200, 221, 21))
        self.weight_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                         "    border-radius: 1px;       \n"
                                         "    height: 5px;              \n"
                                         "    margin: -1px 0;           \n"
                                         "}\n"
                                         "QSlider::handle:horizontal {\n"
                                         "    background-color: rgb(7, 135, 255);\n"
                                         "    border: 1px solid rgb(7, 135, 255);\n"
                                         "    height: 14px;     \n"
                                         "    width: 12px;\n"
                                         "    margin: -4px 0;     \n"
                                         "    border-radius: 5px  ;\n"
                                         "    padding: -4px 0px;  \n"
                                         "}\n"
                                         "QSlider::add-page:horizontal {\n"
                                         "    background: darkgray;\n"
                                         "}\n"
                                         "QSlider::sub-page:horizontal {\n"
                                         "    background: rgb(7, 135, 255);\n"
                                         "}\n"
                                         "color: rgb(255, 255, 255);")
        self.weight_slider.setOrientation(QtCore.Qt.Horizontal)
        self.weight_slider.setObjectName("weight_slider")
        self.water_name = QtWidgets.QLabel(self.centralwidget)
        self.water_name.setGeometry(QtCore.QRect(100, 20, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.water_name.setFont(font)
        self.water_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.water_name.setObjectName("water_name")
        self.weight_lbl = QtWidgets.QLabel(self.centralwidget)
        self.weight_lbl.setGeometry(QtCore.QRect(50, 150, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.weight_lbl.setFont(font)
        self.weight_lbl.setStyleSheet("color:rgb(175, 175, 175)")
        self.weight_lbl.setObjectName("weight_lbl")
        self.male_w = QtWidgets.QRadioButton(self.centralwidget)
        self.male_w.setGeometry(QtCore.QRect(40, 90, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.male_w.setFont(font)
        self.male_w.setStyleSheet("color: rgb(255, 255, 255);")
        self.male_w.setObjectName("male_w")
        self.female_w = QtWidgets.QRadioButton(self.centralwidget)
        self.female_w.setGeometry(QtCore.QRect(170, 90, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.female_w.setFont(font)
        self.female_w.setStyleSheet("color: rgb(255, 255, 255);")
        self.female_w.setObjectName("female_w")
        self.activity_lbl = QtWidgets.QLabel(self.centralwidget)
        self.activity_lbl.setGeometry(QtCore.QRect(50, 280, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.activity_lbl.setFont(font)
        self.activity_lbl.setStyleSheet("color:rgb(175, 175, 175)")
        self.activity_lbl.setObjectName("activity_lbl")
        self.activity_slider = QtWidgets.QSlider(self.centralwidget)
        self.activity_slider.setGeometry(QtCore.QRect(30, 330, 221, 21))
        self.activity_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                           "    border-radius: 1px;       \n"
                                           "    height: 5px;              \n"
                                           "    margin: -1px 0;           \n"
                                           "}\n"
                                           "QSlider::handle:horizontal {\n"
                                           "    background-color: rgb(7, 135, 255);\n"
                                           "    border: 1px solid rgb(7, 135, 255);\n"
                                           "    height: 14px;     \n"
                                           "    width: 12px;\n"
                                           "    margin: -4px 0;     \n"
                                           "    border-radius: 5px  ;\n"
                                           "    padding: -4px 0px;  \n"
                                           "}\n"
                                           "QSlider::add-page:horizontal {\n"
                                           "    background: darkgray;\n"
                                           "}\n"
                                           "QSlider::sub-page:horizontal {\n"
                                           "    background: rgb(7, 135, 255);\n"
                                           "}")
        self.activity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.activity_slider.setObjectName("activity_slider")
        self.weight = QtWidgets.QLabel(self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(270, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.weight.setFont(font)
        self.weight.setStyleSheet("color: rgb(255, 255, 255);")
        self.weight.setText("")
        self.weight.setObjectName("weight")
        self.activity = QtWidgets.QLabel(self.centralwidget)
        self.activity.setGeometry(QtCore.QRect(270, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.activity.setFont(font)
        self.activity.setStyleSheet("color: rgb(255, 255, 255);")
        self.activity.setText("")
        self.activity.setObjectName("activity")
        self.recomendation_lbl = QtWidgets.QLabel(self.centralwidget)
        self.recomendation_lbl.setGeometry(QtCore.QRect(40, 390, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.recomendation_lbl.setFont(font)
        self.recomendation_lbl.setStyleSheet("color: rgb(7, 135, 255);")
        self.recomendation_lbl.setObjectName("recomendation_lbl")
        self.result_water = QtWidgets.QPushButton(self.centralwidget)
        self.result_water.setGeometry(QtCore.QRect(30, 430, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.result_water.setFont(font)
        self.result_water.setStyleSheet("QPushButton {\n"
                                        "    color:  rgb(7, 135, 255);\n"
                                        "    background-color: rgb(50, 50, 50);\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 0px;\n"
                                        "    border-color:  rgb(7, 135, 255);\n"
                                        "    border-color:  rgb(7, 135, 255);\n"
                                        "    min-width: 10em;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "")
        self.result_water.setObjectName("result_water")
        self.water_info = QtWidgets.QTextBrowser(self.centralwidget)
        self.water_info.setGeometry(QtCore.QRect(30, 580, 571, 231))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.water_info.setFont(font)
        self.water_info.setStyleSheet("color: rgb(255, 255, 255);")
        self.water_info.setObjectName("water_info")
        self.image_bottle = QtWidgets.QLabel(self.centralwidget)
        self.image_bottle.setGeometry(QtCore.QRect(310, 70, 500, 500))
        self.image_bottle.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.image_bottle.setText("")
        self.image_bottle.setObjectName("image_bottle")
        MainWindow.setCentralWidget(self.centralwidget)
# diet_page
        self.male_for_diet = QtWidgets.QRadioButton(self.centralwidget)
        self.male_for_diet.setGeometry(QtCore.QRect(20, 120, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.male_for_diet.setFont(font)
        self.male_for_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.male_for_diet.setObjectName("male_for_diet")
        self.gender_lbl = QtWidgets.QLabel(self.centralwidget)
        self.gender_lbl.setGeometry(QtCore.QRect(30, 75, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.gender_lbl.setFont(font)
        self.gender_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.gender_lbl.setObjectName("gender_lbl")
        self.diet_name = QtWidgets.QLabel(self.centralwidget)
        self.diet_name.setGeometry(QtCore.QRect(170, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.diet_name.setFont(font)
        self.diet_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.diet_name.setObjectName("diet_name")
        self.female_for_dieet = QtWidgets.QRadioButton(self.centralwidget)
        self.female_for_dieet.setGeometry(QtCore.QRect(150, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.female_for_dieet.setFont(font)
        self.female_for_dieet.setStyleSheet("color: rgb(255, 255, 255);")
        self.female_for_dieet.setObjectName("female_for_dieet")
        self.height_for_diet = QtWidgets.QLabel(self.centralwidget)
        self.height_for_diet.setGeometry(QtCore.QRect(30, 165, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.height_for_diet.setFont(font)
        self.height_for_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.height_for_diet.setObjectName("height_for_diet")
        self.weigth_for_diet = QtWidgets.QLabel(self.centralwidget)
        self.weigth_for_diet.setGeometry(QtCore.QRect(30, 256, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.weigth_for_diet.setFont(font)
        self.weigth_for_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.weigth_for_diet.setObjectName("weigth_for_diet")
        self.weight_sb_for_diet = QtWidgets.QSpinBox(self.centralwidget)
        self.weight_sb_for_diet.setGeometry(QtCore.QRect(20, 300, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.weight_sb_for_diet.setFont(font)
        self.weight_sb_for_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.weight_sb_for_diet.setMinimum(25)
        self.weight_sb_for_diet.setMaximum(250)
        self.weight_sb_for_diet.setObjectName("weight_sb_for_diet")
        self.height_sb_for_diet = QtWidgets.QSpinBox(self.centralwidget)
        self.height_sb_for_diet.setGeometry(QtCore.QRect(20, 210, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.height_sb_for_diet.setFont(font)
        self.height_sb_for_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.height_sb_for_diet.setMinimum(75)
        self.height_sb_for_diet.setMaximum(220)
        self.height_sb_for_diet.setProperty("value", 75)
        self.height_sb_for_diet.setObjectName("height_sb_for_diet")
        self.count_activity_diet = QtWidgets.QLabel(self.centralwidget)
        self.count_activity_diet.setGeometry(QtCore.QRect(30, 430, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.count_activity_diet.setFont(font)
        self.count_activity_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.count_activity_diet.setObjectName("count_activity_diet")
        self.activity_for_diet = QtWidgets.QComboBox(self.centralwidget)
        self.activity_for_diet.setGeometry(QtCore.QRect(20, 470, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.activity_for_diet.setFont(font)
        self.activity_for_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.activity_for_diet.setObjectName("activity_for_diet")
        self.activity_for_diet.addItem("")
        self.activity_for_diet.addItem("")
        self.activity_for_diet.addItem("")
        self.activity_for_diet.addItem("")
        self.activity_for_diet.addItem("")
        self.result_for_diet = QtWidgets.QPushButton(self.centralwidget)
        self.result_for_diet.setGeometry(QtCore.QRect(380, 520, 301, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.result_for_diet.setFont(font)
        self.result_for_diet.setStyleSheet("QPushButton {\n"
                                           "    color: rgb(214, 200, 4);\n"
                                           "    background-color: rgb(50, 50, 50);\n"
                                           "    border-style: outset;\n"
                                           "    border-width: 1px;\n"
                                           "    border-radius: 0px;\n"
                                           "    border-color: rgb(214, 200, 4);\n"
                                           "    border-color: rgb(214, 200, 4);\n"
                                           "    min-width: 10em;\n"
                                           "    padding: 6px;\n"
                                           "}\n"
                                           "")
        self.result_for_diet.setText("")
        self.result_for_diet.setObjectName("result_for_diet")
        self.sm_lbl = QtWidgets.QLabel(self.centralwidget)
        self.sm_lbl.setGeometry(QtCore.QRect(120, 215, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.sm_lbl.setFont(font)
        self.sm_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.sm_lbl.setObjectName("sm_lbl")
        self.kg_lbl = QtWidgets.QLabel(self.centralwidget)
        self.kg_lbl.setGeometry(QtCore.QRect(120, 305, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.kg_lbl.setFont(font)
        self.kg_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.kg_lbl.setObjectName("kg_lbl")
        self.age_for_diet = QtWidgets.QLabel(self.centralwidget)
        self.age_for_diet.setGeometry(QtCore.QRect(30, 340, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.age_for_diet.setFont(font)
        self.age_for_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.age_for_diet.setObjectName("age_for_diet")
        self.age_sb_for_diet = QtWidgets.QSpinBox(self.centralwidget)
        self.age_sb_for_diet.setGeometry(QtCore.QRect(20, 390, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.age_sb_for_diet.setFont(font)
        self.age_sb_for_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.age_sb_for_diet.setMinimum(1)
        self.age_sb_for_diet.setMaximum(100)
        self.age_sb_for_diet.setProperty("value", 1)
        self.age_sb_for_diet.setObjectName("age_sb_for_diet")
        self.year_lbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.year_lbl_2.setGeometry(QtCore.QRect(120, 395, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.year_lbl_2.setFont(font)
        self.year_lbl_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.year_lbl_2.setObjectName("year_lbl_2")
        self.image_calories = QtWidgets.QLabel(self.centralwidget)
        self.image_calories.setGeometry(QtCore.QRect(330, 80, 350, 350))
        self.image_calories.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.image_calories.setObjectName("image_calories")
        self.get_result_diet = QtWidgets.QPushButton(self.centralwidget)
        self.get_result_diet.setGeometry(QtCore.QRect(70, 530, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.get_result_diet.setFont(font)
        self.get_result_diet.setStyleSheet("QPushButton {\n"
                                           "    color: rgb(214, 200, 4);\n"
                                           "    background-color: rgb(50, 50, 50);\n"
                                           "    border-style: outset;\n"
                                           "    border-width: 3px;\n"
                                           "    border-radius: 10px;\n"
                                           "    border-color: rgb(214, 200, 4);\n"
                                           "    border-color: rgb(214, 200, 4);\n"
                                           "    min-width: 10em;\n"
                                           "    padding: 6px;\n"
                                           "}\n"
                                           "")
        self.get_result_diet.setObjectName("get_result_diet")
        self.your_calories_is_lbl = QtWidgets.QLabel(self.centralwidget)
        self.your_calories_is_lbl.setGeometry(QtCore.QRect(440, 490, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.your_calories_is_lbl.setFont(font)
        self.your_calories_is_lbl.setStyleSheet("color: rgb(214, 200, 4);\n"
                                                "background-color: rgba(0, 0, 0, 0)")
        self.your_calories_is_lbl.setObjectName("your_calories_is_lbl")
        self.info_for_diet = QtWidgets.QTextBrowser(self.centralwidget)
        self.info_for_diet.setGeometry(QtCore.QRect(20, 660, 671, 131))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.info_for_diet.setFont(font)
        self.info_for_diet.setStyleSheet("color: rgb(255, 255, 255);")
        self.info_for_diet.setObjectName("info_for_diet")
        MainWindow.setCentralWidget(self.centralwidget)
#sleeping_page
        self.sleeping_name = QtWidgets.QLabel(self.centralwidget)
        self.sleeping_name.setGeometry(QtCore.QRect(160, 10, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.sleeping_name.setFont(font)
        self.sleeping_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.sleeping_name.setObjectName("sleeping_name")
        self.hours = QtWidgets.QComboBox(self.centralwidget)
        self.hours.setGeometry(QtCore.QRect(240, 100, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.hours.setFont(font)
        self.hours.setStyleSheet("color: rgb(255, 255, 255);")
        self.hours.setObjectName("hours")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.hours.addItem("")
        self.need__wakeup_in = QtWidgets.QLabel(self.centralwidget)
        self.need__wakeup_in.setGeometry(QtCore.QRect(10, 120, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.need__wakeup_in.setFont(font)
        self.need__wakeup_in.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "background-color: rgba(1, 1, 1, 0)")
        self.need__wakeup_in.setObjectName("need__wakeup_in")
        self.minute = QtWidgets.QComboBox(self.centralwidget)
        self.minute.setGeometry(QtCore.QRect(340, 100, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.minute.setFont(font)
        self.minute.setStyleSheet("color: rgb(255, 255, 255);")
        self.minute.setObjectName("minute")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.minute.addItem("")
        self.razdelitel_for_time = QtWidgets.QLabel(self.centralwidget)
        self.razdelitel_for_time.setGeometry(QtCore.QRect(320, 105, 16, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.razdelitel_for_time.setFont(font)
        self.razdelitel_for_time.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "background-color: rgba(1, 1, 1, 0)")
        self.razdelitel_for_time.setObjectName("razdelitel_for_time")
        self.result_sleeping = QtWidgets.QPushButton(self.centralwidget)
        self.result_sleeping.setGeometry(QtCore.QRect(190, 180, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.result_sleeping.setFont(font)
        self.result_sleeping.setStyleSheet("QPushButton {\n"
                                           "    color: rgb(176, 176, 176);\n"
                                           "    background-color: rgb(50, 50, 50);\n"
                                           "    border-style: outset;\n"
                                           "    border-width: 2px;\n"
                                           "    border-radius: 7px;\n"
                                           "    border-color: rgb(176, 176, 176);\n"
                                           "    border-color: rgb(79, 79, 79);\n"
                                           "    min-width: 10em;\n"
                                           "    padding: 6px;\n"
                                           "}\n"
                                           "")
        self.result_sleeping.setObjectName("result_sleeping")
        self.or_lbl = QtWidgets.QLabel(self.centralwidget)
        self.or_lbl.setGeometry(QtCore.QRect(290, 300, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.or_lbl.setFont(font)
        self.or_lbl.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "background-color: rgba(1, 1, 1, 0)")
        self.or_lbl.setObjectName("or_lbl")
        self.when_wakeup_if = QtWidgets.QLabel(self.centralwidget)
        self.when_wakeup_if.setGeometry(QtCore.QRect(50, 360, 591, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.when_wakeup_if.setFont(font)
        self.when_wakeup_if.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color: rgba(1, 1, 1, 0)")
        self.when_wakeup_if.setObjectName("when_wakeup_if")
        self.result_now_sleeping = QtWidgets.QPushButton(self.centralwidget)
        self.result_now_sleeping.setGeometry(QtCore.QRect(190, 440, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.result_now_sleeping.setFont(font)
        self.result_now_sleeping.setStyleSheet("QPushButton {\n"
                                               "    color: rgb(176, 176, 176);\n"
                                               "    background-color: rgb(50, 50, 50);\n"
                                               "    border-style: outset;\n"
                                               "    border-width: 2px;\n"
                                               "    border-radius: 7px;\n"
                                               "    border-color: rgb(176, 176, 176);\n"
                                               "    border-color: rgb(79, 79, 79);\n"
                                               "    min-width: 10em;\n"
                                               "    padding: 6px;\n"
                                               "}\n"
                                               "")
        self.result_now_sleeping.setObjectName("result_now_sleeping")
        self.time1 = QtWidgets.QPushButton(self.centralwidget)
        self.time1.setGeometry(QtCore.QRect(60, 630, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.time1.setFont(font)
        self.time1.setStyleSheet("QPushButton {\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgb(50, 50, 50);\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 7px;\n"
                                 "    border-color: rgb(12, 28, 255);\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;\n"
                                 "}\n"
                                 "")
        self.time1.setText("")
        self.time1.setObjectName("time1")
        self.time4 = QtWidgets.QPushButton(self.centralwidget)
        self.time4.setGeometry(QtCore.QRect(60, 730, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.time4.setFont(font)
        self.time4.setStyleSheet("QPushButton {\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgb(50, 50, 50);\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 7px;\n"
                                 "    border-color: rgb(12, 28, 255);\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;\n"
                                 "}\n"
                                 "")
        self.time4.setText("")
        self.time4.setObjectName("time4")
        self.time2 = QtWidgets.QPushButton(self.centralwidget)
        self.time2.setGeometry(QtCore.QRect(260, 630, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.time2.setFont(font)
        self.time2.setStyleSheet("QPushButton {\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgb(50, 50, 50);\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 7px;\n"
                                 "    border-color: rgb(12, 28, 255);\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;\n"
                                 "}\n"
                                 "")
        self.time2.setText("")
        self.time2.setObjectName("time2")
        self.time3 = QtWidgets.QPushButton(self.centralwidget)
        self.time3.setGeometry(QtCore.QRect(460, 630, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.time3.setFont(font)
        self.time3.setStyleSheet("QPushButton {\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgb(50, 50, 50);\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 7px;\n"
                                 "    border-color: rgb(12, 28, 255);\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;\n"
                                 "}\n"
                                 "")
        self.time3.setText("")
        self.time3.setObjectName("time3")
        self.time5 = QtWidgets.QPushButton(self.centralwidget)
        self.time5.setGeometry(QtCore.QRect(260, 730, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.time5.setFont(font)
        self.time5.setStyleSheet("QPushButton {\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgb(50, 50, 50);\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 7px;\n"
                                 "    border-color: rgb(12, 28, 255);\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;\n"
                                 "}\n"
                                 "")
        self.time5.setText("")
        self.time5.setObjectName("time5")
        self.time6 = QtWidgets.QPushButton(self.centralwidget)
        self.time6.setGeometry(QtCore.QRect(460, 730, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.time6.setFont(font)
        self.time6.setStyleSheet("QPushButton {\n"
                                 "    color: rgb(255, 255, 255);\n"
                                 "    background-color: rgb(50, 50, 50);\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 7px;\n"
                                 "    border-color: rgb(12, 28, 255);\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;\n"
                                 "}\n"
                                 "")
        self.time6.setText("")
        self.time6.setObjectName("time6")
        self.image_sleeping = QtWidgets.QLabel(self.centralwidget)
        self.image_sleeping.setGeometry(QtCore.QRect(460, 80, 230, 230))
        self.image_sleeping.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.image_sleeping.setText("")
        self.image_sleeping.setObjectName("image_sleeping")
        self.go_bed_in = QtWidgets.QLabel(self.centralwidget)
        self.go_bed_in.setGeometry(QtCore.QRect(240, 580, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.go_bed_in.setFont(font)
        self.go_bed_in.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "background-color: rgba(1, 1, 1, 0)")
        self.go_bed_in.setObjectName("go_bed_in")
        MainWindow.setCentralWidget(self.centralwidget)
# profile_page
        self.profile_fon = QtWidgets.QLabel(self.centralwidget)
        self.profile_fon.setGeometry(QtCore.QRect(0, 0, 701, 201))
        self.profile_fon.setStyleSheet("background-color: rgb(97, 97, 97);")
        self.profile_fon.setText("")
        self.profile_fon.setObjectName("profile_fon")

        self.name_surname = QtWidgets.QLabel(self.centralwidget)
        self.name_surname.setGeometry(QtCore.QRect(170, 60, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name_surname.setFont(font)
        self.name_surname.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                        "color: rgb(255, 255, 255);")
        self.name_surname.setObjectName("name_surname")
        self.fit_lvl = QtWidgets.QLabel(self.centralwidget)
        self.fit_lvl.setGeometry(QtCore.QRect(170, 100, 106, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fit_lvl.setFont(font)
        self.fit_lvl.setStyleSheet("background-color: rgb(165, 165, 165);")
        self.fit_lvl.setText("")
        self.fit_lvl.setObjectName("fit_lvl")
        self.physic_data_lbl = QtWidgets.QLabel(self.centralwidget)
        self.physic_data_lbl.setGeometry(QtCore.QRect(230, 210, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.physic_data_lbl.setFont(font)
        self.physic_data_lbl.setStyleSheet("color: rgba(255, 255, 255);\n"
                                           "background-color: rgba(1, 1, 1, 0)")
        self.physic_data_lbl.setObjectName("physic_data_lbl")
        self.gender_user_lbl = QtWidgets.QLabel(self.centralwidget)
        self.gender_user_lbl.setGeometry(QtCore.QRect(80, 280, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gender_user_lbl.setFont(font)
        self.gender_user_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.gender_user_lbl.setObjectName("gender_user_lbl")
        self.weight_user_lbl = QtWidgets.QLabel(self.centralwidget)
        self.weight_user_lbl.setGeometry(QtCore.QRect(320, 280, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.weight_user_lbl.setFont(font)
        self.weight_user_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.weight_user_lbl.setObjectName("weight_user_lbl")
        self.weight_user = QtWidgets.QPushButton(self.centralwidget)
        self.weight_user.setGeometry(QtCore.QRect(250, 330, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setStrikeOut(False)
        self.weight_user.setFont(font)
        self.weight_user.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    border-style: outset;\n"
                                       "    border-width: 3px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: rgb(255, 0, 0);\n"
                                       "    border-color: rgb(255, 255, 255);\n"
                                       "    min-width: 10em;\n"
                                       "    padding: 6px;\n"
                                       "}\n"
                                       "")
        self.weight_user.setObjectName("weight_user")
        self.height_user = QtWidgets.QPushButton(self.centralwidget)
        self.height_user.setGeometry(QtCore.QRect(480, 330, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setStrikeOut(False)
        self.height_user.setFont(font)
        self.height_user.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    border-style: outset;\n"
                                       "    border-width: 3px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: rgb(255, 0, 0);\n"
                                       "    border-color: rgb(255, 255, 255);\n"
                                       "    min-width: 10em;\n"
                                       "    padding: 6px;\n"
                                       "}\n"
                                       "")
        self.height_user.setObjectName("height_user")
        self.height_user_lbl = QtWidgets.QLabel(self.centralwidget)
        self.height_user_lbl.setGeometry(QtCore.QRect(550, 280, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.height_user_lbl.setFont(font)
        self.height_user_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.height_user_lbl.setObjectName("height_user_lbl")
        self.lvl_user_lbl = QtWidgets.QLabel(self.centralwidget)
        self.lvl_user_lbl.setGeometry(QtCore.QRect(60, 490, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lvl_user_lbl.setFont(font)
        self.lvl_user_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.lvl_user_lbl.setObjectName("lvl_user_lbl")
        self.gender_user = QtWidgets.QPushButton(self.centralwidget)
        self.gender_user.setGeometry(QtCore.QRect(20, 330, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setStrikeOut(False)
        self.gender_user.setFont(font)
        self.gender_user.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    border-style: outset;\n"
                                       "    border-width: 3px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: rgb(255, 0, 0);\n"
                                       "    border-color: rgb(255, 255, 255);\n"
                                       "    min-width: 10em;\n"
                                       "    padding: 6px;\n"
                                       "}\n"
                                       "")
        self.gender_user.setObjectName("gender_user")
        self.lvl_user = QtWidgets.QPushButton(self.centralwidget)
        self.lvl_user.setGeometry(QtCore.QRect(20, 540, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setStrikeOut(False)
        self.lvl_user.setFont(font)
        self.lvl_user.setStyleSheet("QPushButton {\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    background-color: rgb(50, 50, 50);\n"
                                    "    border-style: outset;\n"
                                    "    border-width: 3px;\n"
                                    "    border-radius: 10px;\n"
                                    "    border-color: rgb(255, 0, 0);\n"
                                    "    border-color: rgb(255, 255, 255);\n"
                                    "    min-width: 10em;\n"
                                    "    padding: 6px;\n"
                                    "}\n"
                                    "")
        self.lvl_user.setObjectName("lvl_user")
        self.goal_user = QtWidgets.QPushButton(self.centralwidget)
        self.goal_user.setGeometry(QtCore.QRect(250, 540, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setStrikeOut(False)
        self.goal_user.setFont(font)
        self.goal_user.setStyleSheet("QPushButton {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(50, 50, 50);\n"
                                     "    border-style: outset;\n"
                                     "    border-width: 3px;\n"
                                     "    border-radius: 10px;\n"
                                     "    border-color: rgb(255, 0, 0);\n"
                                     "    border-color: rgb(255, 255, 255);\n"
                                     "    min-width: 10em;\n"
                                     "    padding: 6px;\n"
                                     "}\n"
                                     "")
        self.goal_user.setObjectName("goal_user")
        self.max_pullups = QtWidgets.QPushButton(self.centralwidget)
        self.max_pullups.setGeometry(QtCore.QRect(480, 540, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.max_pullups.setFont(font)
        self.max_pullups.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    border-style: outset;\n"
                                       "    border-width: 3px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: rgb(255, 0, 0);\n"
                                       "    border-color: rgb(255, 255, 255);\n"
                                       "    min-width: 10em;\n"
                                       "    padding: 6px;\n"
                                       "}\n"
                                       "")
        self.max_pullups.setObjectName("max_pullups")
        self.max_pushups = QtWidgets.QPushButton(self.centralwidget)
        self.max_pushups.setGeometry(QtCore.QRect(20, 750, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.max_pushups.setFont(font)
        self.max_pushups.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    border-style: outset;\n"
                                       "    border-width: 3px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: rgb(255, 0, 0);\n"
                                       "    border-color: rgb(255, 255, 255);\n"
                                       "    min-width: 10em;\n"
                                       "    padding: 6px;\n"
                                       "}\n"
                                       "")
        self.max_pushups.setObjectName("max_pushups")
        self.max_squats = QtWidgets.QPushButton(self.centralwidget)
        self.max_squats.setGeometry(QtCore.QRect(250, 750, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.max_squats.setFont(font)
        self.max_squats.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(50, 50, 50);\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 3px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: rgb(255, 0, 0);\n"
                                      "    border-color: rgb(255, 255, 255);\n"
                                      "    min-width: 10em;\n"
                                      "    padding: 6px;\n"
                                      "}\n"
                                      "")
        self.max_squats.setObjectName("max_squats")
        self.max_dips = QtWidgets.QPushButton(self.centralwidget)
        self.max_dips.setGeometry(QtCore.QRect(480, 750, 201, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setStrikeOut(False)
        self.max_dips.setFont(font)
        self.max_dips.setStyleSheet("QPushButton {\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    background-color: rgb(50, 50, 50);\n"
                                    "    border-style: outset;\n"
                                    "    border-width: 3px;\n"
                                    "    border-radius: 10px;\n"
                                    "    border-color: rgb(255, 0, 0);\n"
                                    "    border-color: rgb(255, 255, 255);\n"
                                    "    min-width: 10em;\n"
                                    "    padding: 6px;\n"
                                    "}\n"
                                    "")
        self.max_dips.setObjectName("max_dips")
        self.goal_user_lbl = QtWidgets.QLabel(self.centralwidget)
        self.goal_user_lbl.setGeometry(QtCore.QRect(310, 490, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.goal_user_lbl.setFont(font)
        self.goal_user_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.goal_user_lbl.setObjectName("goal_user_lbl")
        self.max_pullups_lbl = QtWidgets.QLabel(self.centralwidget)
        self.max_pullups_lbl.setGeometry(QtCore.QRect(470, 490, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.max_pullups_lbl.setFont(font)
        self.max_pullups_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.max_pullups_lbl.setObjectName("max_pullups_lbl")
        self.max_pushups_lbl = QtWidgets.QLabel(self.centralwidget)
        self.max_pushups_lbl.setGeometry(QtCore.QRect(20, 700, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.max_pushups_lbl.setFont(font)
        self.max_pushups_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.max_pushups_lbl.setObjectName("max_pushups_lbl")
        self.max_squats_lbl = QtWidgets.QLabel(self.centralwidget)
        self.max_squats_lbl.setGeometry(QtCore.QRect(250, 700, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.max_squats_lbl.setFont(font)
        self.max_squats_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.max_squats_lbl.setObjectName("max_squats_lbl")
        self.max_dips_lbl = QtWidgets.QLabel(self.centralwidget)
        self.max_dips_lbl.setGeometry(QtCore.QRect(500, 700, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.max_dips_lbl.setFont(font)
        self.max_dips_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.max_dips_lbl.setObjectName("max_dips_lbl")
        self.settings_image = QtWidgets.QLabel(self.centralwidget)
        self.settings_image.setGeometry(QtCore.QRect(570, 80, 32, 32))
        self.settings_image.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.settings_image.setText("")
        self.settings_image.setObjectName("settings_image")
        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_settings.setGeometry(QtCore.QRect(570, 80, 32, 32))
        self.btn_settings.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.btn_settings.setText("")
        self.btn_settings.setObjectName("btn_settings")
        MainWindow.setCentralWidget(self.centralwidget)
# profile_settings
        self.your_profile_lbl = QtWidgets.QLabel(self.centralwidget)
        self.your_profile_lbl.setGeometry(QtCore.QRect(40, 220, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.your_profile_lbl.setFont(font)
        self.your_profile_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.your_profile_lbl.setObjectName("your_profile_lbl")
        self.white_profile_settings = QtWidgets.QLabel(self.centralwidget)
        self.white_profile_settings.setGeometry(QtCore.QRect(-10, 90, 711, 91))
        self.white_profile_settings.setStyleSheet("background-color: rgb(180, 180 ,180)")
        self.white_profile_settings.setText("")
        self.white_profile_settings.setObjectName("white_profile_settings")
        self.us_name_settings = QtWidgets.QLabel(self.centralwidget)
        self.us_name_settings.setGeometry(QtCore.QRect(200, 270, 491, 41))
        self.us_name_settings.setStyleSheet("border-style: outset;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font: 12pt \"Times New Roman\";\n"
                                            "border-width: 1px;")
        self.us_name_settings.setText("")
        self.us_name_settings.setObjectName("us_name_settings")
        self.user_name_settings_lbl = QtWidgets.QLabel(self.centralwidget)
        self.user_name_settings_lbl.setGeometry(QtCore.QRect(30, 280, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.user_name_settings_lbl.setFont(font)
        self.user_name_settings_lbl.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                  "background-color: rgba(1, 1, 1, 0)")
        self.user_name_settings_lbl.setObjectName("user_name_settings_lbl")
        self.email_settings = QtWidgets.QLabel(self.centralwidget)
        self.email_settings.setGeometry(QtCore.QRect(200, 330, 491, 41))
        self.email_settings.setStyleSheet("border-style: outset;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 12pt \"Times New Roman\";\n"
                                          "border-width: 1px;")
        self.email_settings.setText("")
        self.email_settings.setObjectName("email_settings")
        self.name_settings = QtWidgets.QLabel(self.centralwidget)
        self.name_settings.setGeometry(QtCore.QRect(200, 390, 491, 41))
        self.name_settings.setStyleSheet("border-style: outset;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 12pt \"Times New Roman\";\n"
                                         "border-width: 1px;")
        self.name_settings.setText("")
        self.name_settings.setObjectName("name_settings")
        self.email_settings_lbl = QtWidgets.QLabel(self.centralwidget)
        self.email_settings_lbl.setGeometry(QtCore.QRect(30, 340, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.email_settings_lbl.setFont(font)
        self.email_settings_lbl.setStyleSheet("color: rgb(255, 255, 255);\n"
                                              "background-color: rgba(1, 1, 1, 0)")
        self.email_settings_lbl.setObjectName("email_settings_lbl")
        self.name_settings_lbl = QtWidgets.QLabel(self.centralwidget)
        self.name_settings_lbl.setGeometry(QtCore.QRect(30, 400, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name_settings_lbl.setFont(font)
        self.name_settings_lbl.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "background-color: rgba(1, 1, 1, 0)")
        self.name_settings_lbl.setObjectName("name_settings_lbl")
        self.surname_settings_lbl = QtWidgets.QLabel(self.centralwidget)
        self.surname_settings_lbl.setGeometry(QtCore.QRect(30, 460, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.surname_settings_lbl.setFont(font)
        self.surname_settings_lbl.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                "background-color: rgba(1, 1, 1, 0)")
        self.surname_settings_lbl.setObjectName("surname_settings_lbl")
        self.black_profile_settings = QtWidgets.QLabel(self.centralwidget)
        self.black_profile_settings.setGeometry(QtCore.QRect(0, 0, 711, 91))
        self.black_profile_settings.setStyleSheet("background-color: rgb(50, 50, 50)")
        self.black_profile_settings.setText("")
        self.black_profile_settings.setObjectName("black_profile_settings")
        self.country_settings = QtWidgets.QLabel(self.centralwidget)
        self.country_settings.setGeometry(QtCore.QRect(200, 570, 491, 41))
        self.country_settings.setStyleSheet("border-style: outset;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font: 12pt \"Times New Roman\";\n"
                                            "border-width: 1px;")
        self.country_settings.setText("")
        self.country_settings.setObjectName("country_settings")
        self.city_settings_lbl = QtWidgets.QLabel(self.centralwidget)
        self.city_settings_lbl.setGeometry(QtCore.QRect(30, 520, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.city_settings_lbl.setFont(font)
        self.city_settings_lbl.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "background-color: rgba(1, 1, 1, 0)")
        self.city_settings_lbl.setObjectName("city_settings_lbl")
        self.country_settings_lbl = QtWidgets.QLabel(self.centralwidget)
        self.country_settings_lbl.setGeometry(QtCore.QRect(30, 580, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.country_settings_lbl.setFont(font)
        self.country_settings_lbl.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                "background-color: rgba(1, 1, 1, 0)")
        self.country_settings_lbl.setObjectName("country_settings_lbl")
        self.btn_backtoprofile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_backtoprofile.setGeometry(QtCore.QRect(10, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_backtoprofile.setFont(font)
        self.btn_backtoprofile.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "border: none;\n"
                                             "background-color: rgba(1, 1, 1, 0)")
        self.btn_backtoprofile.setObjectName("btn_backtoprofile")
        self.surname_settings = QtWidgets.QLabel(self.centralwidget)
        self.surname_settings.setGeometry(QtCore.QRect(200, 450, 491, 41))
        self.surname_settings.setStyleSheet("border-style: outset;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "font: 12pt \"Times New Roman\";\n"
                                            "border-width: 1px;")
        self.surname_settings.setText("")
        self.surname_settings.setObjectName("surname_settings")
        self.city_settings = QtWidgets.QLabel(self.centralwidget)
        self.city_settings.setGeometry(QtCore.QRect(200, 510, 491, 41))
        self.city_settings.setStyleSheet("border-style: outset;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "font: 12pt \"Times New Roman\";\n"
                                         "border-width: 1px;")
        self.city_settings.setText("")
        self.city_settings.setObjectName("city_settings")
        self.profile_logo = QtWidgets.QPushButton(self.centralwidget)
        self.profile_logo.setGeometry(QtCore.QRect(50, 40, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.profile_logo.setFont(font)
        self.profile_logo.setStyleSheet("border-style: outset;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 55px")
        self.profile_logo.setObjectName("profile_logo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_water.setText(_translate("MainWindow", "Вода"))
        self.btn_d.setText(_translate("MainWindow", "Питание"))
        self.btn_u.setText(_translate("MainWindow", "Профиль"))
        self.btn_s.setText(_translate("MainWindow", "Тренировки"))
        self.btn_work.setText(_translate("MainWindow", "Сон"))
        self.btn_workoutprogram.setText(_translate("MainWindow", "Программы тренировок"))
        self.worklearn_lbl.setText(_translate("MainWindow", "Как правильно тренироваться на"))
        self.btn_power.setText(_translate("MainWindow", "Силу"))
        self.btn_vynosliv.setText(_translate("MainWindow", "Выносливость"))
        self.btn_massa.setText(_translate("MainWindow", "Мышечные объёмы"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.metod_lbl.setText(_translate("MainWindow", "Метод составления"))
        self.count_lbl.setText(_translate("MainWindow", "Частота тренировок"))
        self.btn_creating_pr.setText(_translate("MainWindow", "Составить программу"))
        self.count_of_work.setItemText(0, _translate("MainWindow", "3 раза в неделю"))
        self.count_of_work.setItemText(1, _translate("MainWindow", "6 раз в неделю"))
        self.antog_rb.setText(_translate("MainWindow", "По мышцам антагонистам"))
        self.sinerg_rb.setText(_translate("MainWindow", "По мышщам синергистам"))
        self.btn_backtomainwork.setText(_translate("MainWindow", "<-"))
        self.endurance_info.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">    Силовая выносливость - это способность мышщ поддерживать силу сокращений в процессе продолжительной интенсивной работы.</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">    При тяжёлых нагрузках мышцы &quot;закисляются&quot;. В них нарастают боль и жжение, и в конце концов наступает отказ - они больше не могут сокращаться. Чем дольше вы продержитесь до этого момента, тем лучше у вас развита силовая выносливость</span></p></body></html>"))
        self.backfromendurance.setText(_translate("MainWindow", "<-"))
        self.workonendurance.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">  Тренировка на выносливость включает в себя следующие факторы:</span></p>\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">А) Мышечный отказ должен приходить на 13+ повторе</span></p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Б) Отдых между подходами: 30-45 секунд</span></p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">В) До 5 подходов на каждое упражнение</span></p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Г) Частота проработки мышечной группы: 1 раз в неделю</span></p></body></html>"))
        self.endurance_name.setText(_translate("MainWindow", "Выносливость"))
        self.power_info.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Сила - это навык.</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Доминирующей структурой при тренировке силы является центральная нервная система. Мы учим её отдавать более сильные сигналы мышцам. То есть когда мы тренируем силу - мы не растим мышцы! Мы учим мозг более эффективно использовать те мышцы, которые уже есть.</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Сила - показатель эффективности использования мышц</span></p></body></html>"))
        self.power_name.setText(_translate("MainWindow", "Сила"))
        self.workonpower.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">  Тренировка на силу включает в себя следующие факторы:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">А) Мышечный отказ должен приходить на 1-5 повторе</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Б) Отдых между подходами: 2-4 минуты</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">В) До 10 подходов на каждое упражнение</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Г) Частота проработки мышечной группы: 2-3 раза в неделю</span></p></body></html>"))
        self.backfrompower.setText(_translate("MainWindow", "<-"))
        self.backfrommassa.setText(_translate("MainWindow", "<-"))
        self.massa_name.setText(_translate("MainWindow", "Мышечная масса"))
        self.massa_info.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Вот вроде бы с практической точки зрения ни объём, ни мышечная масса нам не нужна. Вы ведь наверняка видели случаи, когда человек, у которого гораздо меньше мышц, оказывался намного сильнее. Причем не в бою, а именно по силовым показателям.</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Но то, что человек с меньшим мышечным объёмом может быть сильнее - это лишь половина правды. Чем больше у человека мышечных тканей, тем больше его силовой потенциал. Помимо этого мышечный объём улучшает внешний вид</span></p></body></html>"))
        self.workonmassa.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:16pt; font-weight:600; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">  Тренировка на мышечную массу включает в себя следующие факторы:</span></p>\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">А) Мышечный отказ должен приходить на 6-12 повторе</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Б) Отдых между подходами: 1-2 минуты</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">В) До 5 подходов на каждое упражнение</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Г) Частота проработки мышечной группы: 1-2 раза в неделю</span></p>\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Д) Время под нагрузкой: 45 секунд</span></p></body></html>"))
        self.water_name.setText(_translate("MainWindow", "Калькулятор дневного потребления воды"))
        self.weight_lbl.setText(_translate("MainWindow", "Ваш вес"))
        self.male_w.setText(_translate("MainWindow", "Мужской"))
        self.female_w.setText(_translate("MainWindow", "Женский"))
        self.activity_lbl.setText(_translate("MainWindow", "Физическая активность"))
        self.recomendation_lbl.setText(_translate("MainWindow", "Ваша рекомендованная норма:"))
        self.weight.setText(_translate("MainWindow", "20 кг"))
        self.activity.setText(_translate("MainWindow", "0 ч"))
        self.result_water.setText(_translate("MainWindow", "0.6 литра в день"))
        self.water_info.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Вода играет огромную роль в нашей жизни.</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">В течении дня мы постоянно теряем воду с каждым нашим действием. Именно поэтому для нормального функционирования организма запасы воды нужно постоянно восполнять. </span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">В данном калькуляторе производится расчет потребления питьевой воды без учёта других напитков.</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Правильное потребление воды помогает пищеварению, нормализации веса, улучшает цвет и состояние кожи</span></p></body></html>"))
        self.male_for_diet.setText(_translate("MainWindow", "Мужской"))
        self.gender_lbl.setText(_translate("MainWindow", "Пол:"))
        self.diet_name.setText(_translate("MainWindow", "Калькулятор калорий"))
        self.female_for_dieet.setText(_translate("MainWindow", "Женский"))
        self.height_for_diet.setText(_translate("MainWindow", "Рост:"))
        self.weigth_for_diet.setText(_translate("MainWindow", "Вес:"))
        self.count_activity_diet.setText(_translate("MainWindow", "Степень физ. активности"))
        self.activity_for_diet.setItemText(0, _translate("MainWindow", "минимум/отсутствие физ. активности"))
        self.activity_for_diet.setItemText(1, _translate("MainWindow", "1-3 раза в неделю"))
        self.activity_for_diet.setItemText(2, _translate("MainWindow", "3-5 раз в неделю"))
        self.activity_for_diet.setItemText(3, _translate("MainWindow", "6-7 раз в неделю"))
        self.activity_for_diet.setItemText(4, _translate("MainWindow", "каждый день (интенсивно)"))
        self.sm_lbl.setText(_translate("MainWindow", "см"))
        self.kg_lbl.setText(_translate("MainWindow", "кг"))
        self.age_for_diet.setText(_translate("MainWindow", "Возраст:"))
        self.year_lbl_2.setText(_translate("MainWindow", "лет"))
        self.image_calories.setText(_translate("MainWindow", "TextLabel"))
        self.get_result_diet.setText(_translate("MainWindow", "Рассчитать"))
        self.your_calories_is_lbl.setText(_translate("MainWindow", "Ваша суточная норма"))
        self.info_for_diet.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:400;\">Калькулятор калорий позволит вам рассчитать то количество энергии, которое необходимо ежедневно получать вашему организму в зависимости от вашего роста, веса, возраста и степени физической активности (суточная норма калорий).</span></p></body></html>"))
        self.sleeping_name.setText(_translate("MainWindow", "Калькулятор сна"))
        self.hours.setItemText(0, _translate("MainWindow", "00"))
        self.hours.setItemText(1, _translate("MainWindow", "01"))
        self.hours.setItemText(2, _translate("MainWindow", "02"))
        self.hours.setItemText(3, _translate("MainWindow", "03"))
        self.hours.setItemText(4, _translate("MainWindow", "04"))
        self.hours.setItemText(5, _translate("MainWindow", "05"))
        self.hours.setItemText(6, _translate("MainWindow", "06"))
        self.hours.setItemText(7, _translate("MainWindow", "07"))
        self.hours.setItemText(8, _translate("MainWindow", "08"))
        self.hours.setItemText(9, _translate("MainWindow", "09"))
        self.hours.setItemText(10, _translate("MainWindow", "10"))
        self.hours.setItemText(11, _translate("MainWindow", "11"))
        self.hours.setItemText(12, _translate("MainWindow", "12"))
        self.hours.setItemText(13, _translate("MainWindow", "13"))
        self.hours.setItemText(14, _translate("MainWindow", "14"))
        self.hours.setItemText(15, _translate("MainWindow", "15"))
        self.hours.setItemText(16, _translate("MainWindow", "16"))
        self.hours.setItemText(17, _translate("MainWindow", "17"))
        self.hours.setItemText(18, _translate("MainWindow", "18"))
        self.hours.setItemText(19, _translate("MainWindow", "19"))
        self.hours.setItemText(20, _translate("MainWindow", "20"))
        self.hours.setItemText(21, _translate("MainWindow", "21"))
        self.hours.setItemText(22, _translate("MainWindow", "22"))
        self.hours.setItemText(23, _translate("MainWindow", "23"))
        self.need__wakeup_in.setText(_translate("MainWindow", "Нужно проснуться в"))
        self.minute.setItemText(0, _translate("MainWindow", "00"))
        self.minute.setItemText(1, _translate("MainWindow", "05"))
        self.minute.setItemText(2, _translate("MainWindow", "10"))
        self.minute.setItemText(3, _translate("MainWindow", "15"))
        self.minute.setItemText(4, _translate("MainWindow", "20"))
        self.minute.setItemText(5, _translate("MainWindow", "25"))
        self.minute.setItemText(6, _translate("MainWindow", "30"))
        self.minute.setItemText(7, _translate("MainWindow", "35"))
        self.minute.setItemText(8, _translate("MainWindow", "40"))
        self.minute.setItemText(9, _translate("MainWindow", "45"))
        self.minute.setItemText(10, _translate("MainWindow", "50"))
        self.minute.setItemText(11, _translate("MainWindow", "55"))
        self.razdelitel_for_time.setText(_translate("MainWindow", ":"))
        self.result_sleeping.setText(_translate("MainWindow", "Рассчитать"))
        self.or_lbl.setText(_translate("MainWindow", "или"))
        self.when_wakeup_if.setText(_translate("MainWindow", "Во сколько вставать, если я ложусь прямо сейчас..."))
        self.result_now_sleeping.setText(_translate("MainWindow", "Z Z Z"))
        self.go_bed_in.setText(_translate("MainWindow", "Ложитесь спать в:"))
        self.profile_logo.setText(_translate("MainWindow", "RM"))
        self.name_surname.setText(_translate("MainWindow", "Roman Mityakin"))
        self.physic_data_lbl.setText(_translate("MainWindow", "Физические данные"))
        self.gender_user_lbl.setText(_translate("MainWindow", "Пол"))
        self.weight_user_lbl.setText(_translate("MainWindow", "Вес"))
        self.weight_user.setText(_translate("MainWindow", "-"))
        self.height_user.setText(_translate("MainWindow", "-"))
        self.height_user_lbl.setText(_translate("MainWindow", "Рост"))
        self.lvl_user_lbl.setText(_translate("MainWindow", "Уровень"))
        self.gender_user.setText(_translate("MainWindow", "-"))
        self.lvl_user.setText(_translate("MainWindow", "-"))
        self.goal_user.setText(_translate("MainWindow", "-"))
        self.max_pullups.setText(_translate("MainWindow", "-"))
        self.max_pushups.setText(_translate("MainWindow", "-"))
        self.max_squats.setText(_translate("MainWindow", "-"))
        self.max_dips.setText(_translate("MainWindow", "-"))
        self.goal_user_lbl.setText(_translate("MainWindow", "Цель"))
        self.max_pullups_lbl.setText(_translate("MainWindow", "Макс. подтягивания"))
        self.max_pushups_lbl.setText(_translate("MainWindow", "Макс. отжимания"))
        self.max_squats_lbl.setText(_translate("MainWindow", "Макс. приседания"))
        self.max_dips_lbl.setText(_translate("MainWindow", "Макс. брусья"))
        self.your_profile_lbl.setText(_translate("MainWindow", "Ваш профиль"))
        self.user_name_settings_lbl.setText(_translate("MainWindow", "Имя пользователя"))
        self.email_settings_lbl.setText(_translate("MainWindow", "Email"))
        self.name_settings_lbl.setText(_translate("MainWindow", "Имя"))
        self.surname_settings_lbl.setText(_translate("MainWindow", "Фамилия"))
        self.city_settings_lbl.setText(_translate("MainWindow", "Город"))
        self.country_settings_lbl.setText(_translate("MainWindow", "Страна"))
        self.btn_backtoprofile.setText(_translate("MainWindow", "<-"))


class Anketa_design(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 950)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 291, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.male_anketa = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.male_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.male_anketa.setObjectName("male_anketa")
        self.horizontalLayout.addWidget(self.male_anketa)
        self.female_anketa = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.female_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.female_anketa.setObjectName("female_anketa")
        self.info_user_lbl = QLabel('Имя пользователя уже занято. Попробуйте другое', self)
        self.info_user_lbl.setStyleSheet("color: rgb(255, 50, 50);\n"
                                         "background-color: rgba(255, 255, 255, 0);\n"
                                         "font: 75 8pt \"Times New Roman\";")
        self.info_user_lbl.setGeometry(QtCore.QRect(150, 680, 300, 15))
        self.horizontalLayout.addWidget(self.female_anketa)
        self.anketa_gender = QtWidgets.QLabel(self.centralwidget)
        self.anketa_gender.setGeometry(QtCore.QRect(120, 10, 51, 31))
        self.anketa_gender.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.anketa_gender.setObjectName("anketa_gender")
        self.anketa_weight = QtWidgets.QLabel(self.centralwidget)
        self.anketa_weight.setGeometry(QtCore.QRect(360, 10, 51, 31))
        self.anketa_weight.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.anketa_weight.setObjectName("anketa_weight")
        self.weight_sp_anketa = QtWidgets.QSpinBox(self.centralwidget)
        self.weight_sp_anketa.setGeometry(QtCore.QRect(350, 60, 71, 41))
        self.weight_sp_anketa.setStyleSheet("color: white;\n"
"font: 75 16pt \"Times New Roman\";")
        self.weight_sp_anketa.setMinimum(25)
        self.weight_sp_anketa.setMaximum(250)
        self.weight_sp_anketa.setObjectName("weight_sp_anketa")
        self.anketa_height = QtWidgets.QLabel(self.centralwidget)
        self.anketa_height.setGeometry(QtCore.QRect(530, 10, 71, 31))
        self.anketa_height.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.anketa_height.setObjectName("anketa_height")
        self.height_sb_anketa = QtWidgets.QSpinBox(self.centralwidget)
        self.height_sb_anketa.setGeometry(QtCore.QRect(530, 60, 71, 41))
        self.height_sb_anketa.setStyleSheet("color: white;\n"
"font: 75 16pt \"Times New Roman\";")
        self.height_sb_anketa.setMinimum(75)
        self.height_sb_anketa.setMaximum(220)
        self.height_sb_anketa.setObjectName("height_sb_anketa")
        self.kg_anketa = QtWidgets.QLabel(self.centralwidget)
        self.kg_anketa.setGeometry(QtCore.QRect(430, 70, 51, 31))
        self.kg_anketa.setStyleSheet("font: 14pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.kg_anketa.setObjectName("kg_anketa")
        self.sm_anketa = QtWidgets.QLabel(self.centralwidget)
        self.sm_anketa.setGeometry(QtCore.QRect(620, 70, 51, 31))
        self.sm_anketa.setStyleSheet("font: 14pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.sm_anketa.setObjectName("sm_anketa")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 180, 641, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.beginner_anketa = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.beginner_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.beginner_anketa.setObjectName("beginner_anketa")
        self.horizontalLayout_2.addWidget(self.beginner_anketa)
        self.intermediate_anketa = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.intermediate_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.intermediate_anketa.setObjectName("intermediate_anketa")
        self.horizontalLayout_2.addWidget(self.intermediate_anketa)
        self.advanced_anketa = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.advanced_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.advanced_anketa.setObjectName("advanced_anketa")
        self.horizontalLayout_2.addWidget(self.advanced_anketa)
        self.fit_lvl_anketa = QtWidgets.QLabel(self.centralwidget)
        self.fit_lvl_anketa.setGeometry(QtCore.QRect(210, 140, 211, 41))
        self.fit_lvl_anketa.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.fit_lvl_anketa.setObjectName("fit_lvl_anketa")
        self.goal_anketa = QtWidgets.QLabel(self.centralwidget)
        self.goal_anketa.setGeometry(QtCore.QRect(270, 300, 71, 41))
        self.goal_anketa.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.goal_anketa.setObjectName("goal_anketa")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 350, 641, 101))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.massa_anketa = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.massa_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.massa_anketa.setObjectName("massa_anketa")
        self.horizontalLayout_3.addWidget(self.massa_anketa)
        self.strngth_anketa = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.strngth_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.strngth_anketa.setObjectName("strngth_anketa")
        self.horizontalLayout_3.addWidget(self.strngth_anketa)
        self.fat_anketa = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.fat_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 14pt \"Times New Roman\";")
        self.fat_anketa.setObjectName("fat_anketa")
        self.horizontalLayout_3.addWidget(self.fat_anketa)
        self.user_name_ank = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name_ank.setGeometry(QtCore.QRect(150, 640, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.user_name_ank.setFont(font)
        self.user_name_ank.setStyleSheet("color: rgb(255, 255, 255);")
        self.user_name_ank.setText("")
        self.user_name_ank.setObjectName("user_name_ank")
        self.country_ank = QtWidgets.QLineEdit(self.centralwidget)
        self.country_ank.setGeometry(QtCore.QRect(150, 760, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.country_ank.setFont(font)
        self.country_ank.setStyleSheet("color: rgb(255, 255, 255);")
        self.country_ank.setText("")
        self.country_ank.setObjectName("country_ank")
        self.city_ank = QtWidgets.QLineEdit(self.centralwidget)
        self.city_ank.setGeometry(QtCore.QRect(150, 820, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.city_ank.setFont(font)
        self.city_ank.setStyleSheet("color: rgb(255, 255, 255);")
        self.city_ank.setText("")
        self.city_ank.setObjectName("city_ank")
        self.fullname_ank = QtWidgets.QLineEdit(self.centralwidget)
        self.fullname_ank.setGeometry(QtCore.QRect(150, 700, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.fullname_ank.setFont(font)
        self.fullname_ank.setStyleSheet("color: rgb(255, 255, 255);")
        self.fullname_ank.setText("")
        self.fullname_ank.setObjectName("fullname_ank")
        self.max_data_anketa = QtWidgets.QLabel(self.centralwidget)
        self.max_data_anketa.setGeometry(QtCore.QRect(50, 470, 671, 41))
        self.max_data_anketa.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.max_data_anketa.setObjectName("max_data_anketa")
        self.pull_anketa = QtWidgets.QSpinBox(self.centralwidget)
        self.pull_anketa.setGeometry(QtCore.QRect(60, 550, 71, 41))
        self.pull_anketa.setStyleSheet("color: white;\n"
"font: 75 16pt \"Times New Roman\";")
        self.pull_anketa.setMinimum(0)
        self.pull_anketa.setMaximum(999)
        self.pull_anketa.setProperty("value", 0)
        self.pull_anketa.setObjectName("pull_anketa")
        self.push_anketa = QtWidgets.QSpinBox(self.centralwidget)
        self.push_anketa.setGeometry(QtCore.QRect(230, 550, 71, 41))
        self.push_anketa.setStyleSheet("color: white;\n"
"font: 75 16pt \"Times New Roman\";")
        self.push_anketa.setMinimum(0)
        self.push_anketa.setMaximum(999)
        self.push_anketa.setProperty("value", 0)
        self.push_anketa.setObjectName("push_anketa")
        self.squats_anketa = QtWidgets.QSpinBox(self.centralwidget)
        self.squats_anketa.setGeometry(QtCore.QRect(400, 550, 71, 41))
        self.squats_anketa.setStyleSheet("color: white;\n"
"font: 75 16pt \"Times New Roman\";")
        self.squats_anketa.setMinimum(0)
        self.squats_anketa.setMaximum(999)
        self.squats_anketa.setProperty("value", 0)
        self.squats_anketa.setObjectName("squats_anketa")
        self.dips_anketa = QtWidgets.QSpinBox(self.centralwidget)
        self.dips_anketa.setGeometry(QtCore.QRect(570, 550, 71, 41))
        self.dips_anketa.setStyleSheet("color: white;\n"
"font: 75 16pt \"Times New Roman\";")
        self.dips_anketa.setMinimum(0)
        self.dips_anketa.setMaximum(999)
        self.dips_anketa.setProperty("value", 0)
        self.dips_anketa.setObjectName("dips_anketa")
        self.slash1 = QtWidgets.QLabel(self.centralwidget)
        self.slash1.setGeometry(QtCore.QRect(170, 550, 21, 41))
        self.slash1.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.slash1.setObjectName("slash1")
        self.slash2 = QtWidgets.QLabel(self.centralwidget)
        self.slash2.setGeometry(QtCore.QRect(340, 550, 21, 41))
        self.slash2.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.slash2.setObjectName("slash2")
        self.slash3 = QtWidgets.QLabel(self.centralwidget)
        self.slash3.setGeometry(QtCore.QRect(510, 550, 21, 41))
        self.slash3.setStyleSheet("font: 16pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.slash3.setObjectName("slash3")
        self.user_name_lbl_anketa = QtWidgets.QLabel(self.centralwidget)
        self.user_name_lbl_anketa.setGeometry(QtCore.QRect(10, 650, 141, 21))
        self.user_name_lbl_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 10pt \"Times New Roman\";")
        self.user_name_lbl_anketa.setObjectName("user_name_lbl_anketa")
        self.fullname_lbl_anketa = QtWidgets.QLabel(self.centralwidget)
        self.fullname_lbl_anketa.setGeometry(QtCore.QRect(30, 710, 141, 21))
        self.fullname_lbl_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 10pt \"Times New Roman\";")
        self.fullname_lbl_anketa.setObjectName("fullname_lbl_anketa")
        self.country_lbl_anketa = QtWidgets.QLabel(self.centralwidget)
        self.country_lbl_anketa.setGeometry(QtCore.QRect(90, 770, 61, 21))
        self.country_lbl_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 10pt \"Times New Roman\";")
        self.country_lbl_anketa.setObjectName("country_lbl_anketa")
        self.city_lbl_anketa = QtWidgets.QLabel(self.centralwidget)
        self.city_lbl_anketa.setGeometry(QtCore.QRect(90, 830, 51, 21))
        self.city_lbl_anketa.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 10pt \"Times New Roman\";")
        self.city_lbl_anketa.setObjectName("city_lbl_anketa")
        self.btn_ready = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ready.setGeometry(QtCore.QRect(50, 880, 601, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setStrikeOut(False)
        self.btn_ready.setFont(font)
        self.btn_ready.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(100, 200, 255);\n"
"    border-color: rgb(0, 255, 255);\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"")
        self.btn_ready.setObjectName("btn_log")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.male_anketa.setText(_translate("MainWindow", "Мужской"))
        self.female_anketa.setText(_translate("MainWindow", "Женский"))
        self.anketa_gender.setText(_translate("MainWindow", "Пол"))
        self.anketa_weight.setText(_translate("MainWindow", "Вес"))
        self.anketa_height.setText(_translate("MainWindow", "Рост"))
        self.kg_anketa.setText(_translate("MainWindow", "кг"))
        self.sm_anketa.setText(_translate("MainWindow", "см"))
        self.beginner_anketa.setText(_translate("MainWindow", "Начинающий"))
        self.intermediate_anketa.setText(_translate("MainWindow", "Базовый"))
        self.advanced_anketa.setText(_translate("MainWindow", "Продвинутый"))
        self.fit_lvl_anketa.setText(_translate("MainWindow", "Фитнес уровень"))
        self.goal_anketa.setText(_translate("MainWindow", "Цель"))
        self.massa_anketa.setText(_translate("MainWindow", "Набор массы"))
        self.strngth_anketa.setText(_translate("MainWindow", "Прокачка силы"))
        self.fat_anketa.setText(_translate("MainWindow", "Сжигание жира"))
        self.max_data_anketa.setText(_translate("MainWindow", "Макс. подтягивания/отжимания/приседания/брусья"))
        self.slash1.setText(_translate("MainWindow", "/"))
        self.slash2.setText(_translate("MainWindow", "/"))
        self.slash3.setText(_translate("MainWindow", "/"))
        self.user_name_lbl_anketa.setText(_translate("MainWindow", "Имя пользователя"))
        self.fullname_lbl_anketa.setText(_translate("MainWindow", "Имя и Фамилия"))
        self.country_lbl_anketa.setText(_translate("MainWindow", "Страна"))
        self.city_lbl_anketa.setText(_translate("MainWindow", "Город"))
        self.btn_ready.setText(_translate("MainWindow", "Готово"))

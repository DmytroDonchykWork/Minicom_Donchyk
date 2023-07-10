from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(810, 600)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 70))
        palette.setColor(QPalette.WindowText, QColor(255, 191, 0))
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.comboBox1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox1.setGeometry(QtCore.QRect(150, 530, 200, 20))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(11)
        self.comboBox1.setFont(font)
        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 0, 790, 520))
        self.textBrowser.setObjectName("textBrowser")

        self.ttyUSB0_port_radiobutton = QtWidgets.QRadioButton(self.centralwidget)
        self.ttyUSB0_port_radiobutton.setGeometry(QtCore.QRect(510, 530, 112, 20))
        self.ttyUSB0_port_radiobutton.setObjectName("ttyUSB0_port_radiobutton")
        self.ttyUSB0_port_radiobutton.setChecked(True)

        self.ttyS0_port_radiobutton = QtWidgets.QRadioButton(self.centralwidget)
        self.ttyS0_port_radiobutton.setGeometry(QtCore.QRect(600, 530, 112, 20))
        self.ttyS0_port_radiobutton.setObjectName("ttyS0_port_radiobutton")

        self.lineEdit_command_line = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_command_line.setGeometry(QtCore.QRect(170, 560, 620, 20))
        self.lineEdit_command_line.setObjectName("lineEdit_command_line")

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 530, 150, 20))
        self.label2.setObjectName("label2")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 560, 150, 20))
        self.label1.setObjectName("label1")

        self.button1_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.button1_Submit.setGeometry(QtCore.QRect(670, 527, 120, 25))
        self.button1_Submit.setObjectName("button1_Submit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "This minicom is mine"))

        self.ttyUSB0_port_radiobutton.setText(_translate("MainWindow", "ttyUSB0"))
        self.ttyS0_port_radiobutton.setText(_translate("MainWindow", "ttyS0"))

        self.label1.setText(_translate("MainWindow", "Enter your command:"))
        self.label2.setText(_translate("MainWindow", "Select boudrate:"))

        self.button1_Submit.setText(_translate("MainWindow", "Connect to port"))

        self.comboBox1.setItemText(0, _translate("MainWindow", "230400"))
        self.comboBox1.setItemText(1, _translate("MainWindow", "115200"))
        self.comboBox1.setItemText(2, _translate("MainWindow", "57600"))

    def update_log(self, data):
        self.textBrowser.append(data)

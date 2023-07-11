from PyQt5 import QtWidgets

from Main_window_minicon import Ui_MainWindow


class View(Ui_MainWindow):
    def __init__(self):
        self.mainwindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self, MainWindow=self.mainwindow)

    def update_log(self, data):
        self.textBrowser.append(data)

    def send_command_to_serial(self):
        command = self.lineEdit_command_line.text()
        self.serial_reader_thread.send_command(command)

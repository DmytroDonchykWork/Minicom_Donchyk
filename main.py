from PyQt5 import QtWidgets

from main_controller import Controller
from main_view import View

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    view = View()
    view.setupUi(MainWindow)
    controller = Controller(view)

    controller.start_serial_reading()

    view.button1_Submit.clicked.connect(controller.start_serial_reading)
    view.lineEdit_command_line.returnPressed.connect(controller.send_command_to_serial)

    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets

from main_controller import Controller
from main_model import SerialReaderThread
from main_view import View

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    thread = SerialReaderThread()
    view = View()
    controller = Controller(view, thread)

    view.button1_Submit.clicked.connect(controller.start_serial_reading)
    view.lineEdit_command_line.returnPressed.connect(controller.send_command_to_serial)

    view.mainwindow.show()
    sys.exit(app.exec_())

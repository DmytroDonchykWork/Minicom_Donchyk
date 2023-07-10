from PyQt5 import QtWidgets

from main_model import SerialReaderThread
from main_view import Ui_MainWindow


def start_serial_reading():
    # It'll be better to make ports choose by comboBox, as I did with a baudrate, but I'd like to make various items
    # right now. If it's not necessary, I can refactor it from radioButtons to a comboBox as well.
    ports = {
        'port_ttyUSB0': '/dev/ttyUSB0',
        'port_ttyS0': '/dev/ttyS0'
    }

    if ui.ttyUSB0_port_radiobutton.isChecked():
        port = ports['port_ttyUSB0']

    if ui.ttyS0_port_radiobutton.isChecked():
        port = ports['port_ttyS0']

    baudrate = int(ui.comboBox1.currentText())

    timeout = 1

    ui.serial_reader_thread = SerialReaderThread(port, baudrate, timeout)
    ui.serial_reader_thread.data_received.connect(ui.update_log)
    ui.serial_reader_thread.start()


def closeEvent(ui, event):
    if ui.serial_reader_thread is not None and ui.serial_reader_thread.isRunning():
        ui.serial_reader_thread.terminate()
        ui.serial_reader_thread.wait()
    event.accept()


def send_command_to_serial():
    command = ui.lineEdit_command_line.text()
    ui.serial_reader_thread.send_command(command)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.button1_Submit.clicked.connect(start_serial_reading)
    ui.lineEdit_command_line.returnPressed.connect(send_command_to_serial)

    MainWindow.show()
    sys.exit(app.exec_())

from main_model import SerialReaderThread


class Controller:
    def __init__(self, view):
        self.view = view

    def start_serial_reading(self):
        # It'll be better to make ports choose by comboBox, as I did with a baudrate, but I'd like to make various items
        # right now. If it's not necessary, I can refactor it from radioButtons to a comboBox as well.
        ports = {
            'port_ttyUSB0': '/dev/ttyUSB0',
            'port_ttyS0': '/dev/ttyS0'
        }

        if self.view.ttyUSB0_port_radiobutton.isChecked():
            port = ports['port_ttyUSB0']

        if self.view.ttyS0_port_radiobutton.isChecked():
            port = ports['port_ttyS0']

        baudrate = int(self.view.comboBox1.currentText())

        timeout = 1

        self.view.serial_reader_thread = SerialReaderThread(port, baudrate, timeout)
        self.view.serial_reader_thread.data_received.connect(self.view.update_log)
        self.view.serial_reader_thread.start()

    def closeEvent(self, event):
        if self.view.serial_reader_thread is not None and self.view.serial_reader_thread.isRunning():
            self.view.serial_reader_thread.terminate()
            self.view.serial_reader_thread.wait()
        event.accept()

    def send_command_to_serial(self):
        command = self.view.lineEdit_command_line.text()
        self.view.serial_reader_thread.send_command(command)

import serial

from PyQt5.QtCore import QThread, pyqtSignal


class SerialReaderThread(QThread):
    data_received = pyqtSignal(str)

    def __init__(self, port, baudrate, timeout):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

    def run(self):
        ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        while True:
            try:
                data = ser.readline().decode('utf-8').strip()
            except UnicodeDecodeError:
                self.data_received.emit("Baud rate error - change baud rate to a valuable one!")
                break
            self.data_received.emit(data.replace("\r", ""))

    def send_command(self, command):
        ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
        ser.write(command.encode() + b"\r")

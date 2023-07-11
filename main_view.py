from Main_window_minicon import Ui_MainWindow


class View(Ui_MainWindow):

    def update_log(self, data):
        self.textBrowser.append(data)

    def send_command_to_serial(self, serial_reader_thread):
        command = self.lineEdit_command_line.text()
        serial_reader_thread.send_command(command)

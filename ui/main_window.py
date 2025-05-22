from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)
        self.resize(800, 600)
        self.setWindowTitle('Мастер уведомлений')
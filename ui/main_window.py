from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(550, 250)
        self.setMaximumSize(750,250)
        self.setWindowTitle('Мастер уведомлений')
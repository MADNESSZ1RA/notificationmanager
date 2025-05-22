import os
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtCore import QUrl
from ui.bridge import AppBridge


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Уведомлятор")
        self.resize(800, 600)

        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        self.channel = QWebChannel()
        self.bridge = AppBridge()
        self.bridge.view = self.view

        self.channel.registerObject("bridge", self.bridge)
        self.view.page().setWebChannel(self.channel)

        # Абсолютный путь до index.html
        html_path = os.path.abspath("ui/pages/index.html")
        self.view.load(QUrl.fromLocalFile(html_path))

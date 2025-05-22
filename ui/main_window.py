from PySide6.QtWidgets import QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtCore import QUrl
from pathlib import Path

from ui.bridge import AppBridge

from src.notifications import Notifier
from src.notification_creator import NotificationCreator
from src.notification_storage import NotificationStorage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Уведомлятор")
        self.resize(800, 600)

        notifier = Notifier()
        storage = NotificationStorage()
        creator = NotificationCreator(storage, notifier)

        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        self.channel = QWebChannel()
        self.bridge = AppBridge(creator)

        self.channel.registerObject("bridge", self.bridge)
        self.view.page().setWebChannel(self.channel)

        html_path = Path(__file__).parent / "pages" / "index.html"
        self.view.load(QUrl.fromLocalFile(str(html_path.resolve())))

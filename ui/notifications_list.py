from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from PySide6.QtCore import Qt

from ui.pages.ui_notifications_list import Ui_notificationLayout
from ui.notification import NotificationCard
from src.notification_manager import NotificationStorage


class NotificationsList(QWidget, Ui_notificationLayout):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.setupUi(self)

        self.main_window = main_window
        self.exitButton.clicked.connect(self.go_back)

        if self.scrollAreaWidgetContents.layout() is None:
            self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        else:
            self.scrollLayout = self.scrollAreaWidgetContents.layout()

        self.scrollLayout.setSpacing(8)
        self.scrollLayout.setContentsMargins(6, 6, 6, 6)

        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.refresh()

    def go_back(self):
        from ui.index import IndexPage
        self.main_window.setCentralWidget(IndexPage(self.main_window))

    def refresh(self):
        while self.scrollLayout.count():
            item = self.scrollLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)
                widget.deleteLater()

        for n in sorted(NotificationStorage.load(), key=lambda x: x["time"]):
            card = NotificationCard(n, self, self.scrollAreaWidgetContents)
            self.scrollLayout.addWidget(card)

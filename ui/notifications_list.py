from PySide6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from ui.pages.ui_notifications_list import Ui_notificationLayout
from ui.notification import NotificationCard
from src.notification_manager import NotificationStorage


class NotificationsList(QWidget, Ui_notificationLayout):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

        self.exitButton.clicked.connect(self.back)

        self.scrollLayout: QVBoxLayout = self.verticalLayout_2
        self.scrollLayout.setSpacing(6)

        self.refresh()

    def back(self):
        from ui.index import IndexPage
        self.main_window.setCentralWidget(IndexPage(self.main_window))

    def refresh(self):
        while self.scrollLayout.count():
            item = self.scrollLayout.takeAt(0)
            if w := item.widget():
                w.setParent(None)
                w.deleteLater()

        for n in sorted(NotificationStorage.load(), key=lambda x: x["time"]):
            self.scrollLayout.addWidget(NotificationCard(n, self))

        self.scrollLayout.addStretch(1)

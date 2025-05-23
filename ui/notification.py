from PySide6.QtWidgets import QWidget, QMessageBox, QSizePolicy
from ui.pages.ui_notification import Ui_notificationWidget
from src.notification_manager import NotificationStorage


class NotificationCard(QWidget, Ui_notificationWidget):
    def __init__(self, data: dict, list_page: QWidget, parent: QWidget | None):
        super().__init__(parent)
        self.setupUi(self)

        self.data = data
        self.list_page = list_page

        self.type.setText(f"Тип: {data.get('type', '')}")
        self.time.setText(f"Время: {data.get('time', '')}")
        self.title.setText(f"Заголовок: {data.get('title', '')}")
        self.description.setText(f"Сообщение: {data.get('message', '')}")

        self.setMinimumHeight(95)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

        self.deleteButton.clicked.connect(self.delete_me)

    def delete_me(self):
        if QMessageBox.question(
            self, "Удалить", "Удалить это уведомление?",
            QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.No:
            return

        NotificationStorage.delete(self.data["id"])
        self.setParent(None)
        self.deleteLater()
        self.list_page.refresh()

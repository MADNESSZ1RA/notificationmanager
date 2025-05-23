from PySide6.QtWidgets import QWidget, QMessageBox
from ui.pages.ui_notification import Ui_notificationWidget
from src.notification_manager import NotificationStorage


class NotificationCard(QWidget, Ui_notificationWidget):
    def __init__(self, data: dict, list_page: QWidget):
        super().__init__(list_page)
        self.setupUi(self)

        self.data = data
        self.list_page = list_page

        self.type.setText(f"Тип: {data.get('type', '')}")
        self.time.setText(f"Время: {data.get('time', '')}")
        self.title.setText(data.get('title', '—'))
        self.description.setText(data.get('message', '—'))

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

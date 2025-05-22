import sys

from datetime import datetime, timedelta

from src.notifications import Notifier, NotificationManager
from src.notification_storage import NotificationStorage
from src.notification_creator import NotificationCreator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    # notifier = Notifier()
    # storage = NotificationStorage()
    # creator = NotificationCreator(storage, notifier)

    # storage.clear_all()

    # # Примеры: текущее время + N минут
    # now = datetime.now()
    # creator.create_scheduled_notification(
    #     (now + timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M"),
    #     "Уведомление 1",
    #     "Через 2 минуты")

    # creator.create_scheduled_notification(
    #     (now + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M"),
    #     "Уведомление 2",
    #     "Через 1 минуту")

    # # === Запуск всех уведомлений по времени ===
    # notifications = creator.load_notifications()
    # for notification_strategy in notifications:
    #     manager = NotificationManager(notification_strategy)
    #     manager.run()

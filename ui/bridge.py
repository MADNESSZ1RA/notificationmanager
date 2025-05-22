from PySide6.QtCore import QObject, Slot
from src.notifications import NotificationManager

class AppBridge(QObject):
    def __init__(self, creator):
        super().__init__()
        self.creator = creator

    @Slot(str, str, str)
    def addScheduledNotification(self, time_str, title, message):
        print(f"[Scheduled] В {time_str} — {title}: {message}")
        self.creator.create_scheduled_notification(time_str, title, message)

    @Slot(int, str, str)
    def addDelayedNotification(self, delay_seconds, title, message):
        print(f"[Delayed] Через {delay_seconds} секунд — {title}: {message}")
        self.creator.create_delayed_notification(delay_seconds, title, message)

    @Slot()
    def startAllNotifications(self):
        print("[!] Запуск уведомлений...")
        notifications = self.creator.load_notifications()

        notifications.sort(key=lambda n: getattr(n, "target_time", "00:00"))

        for notification in notifications:
            manager = NotificationManager(notification)
            manager.run()

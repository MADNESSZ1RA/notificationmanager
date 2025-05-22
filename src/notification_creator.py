from datetime import datetime, timedelta

from src.notification_storage import NotificationStorage
from src.notifications import Notifier, DelayedNotification, ScheduledNotification, NotificationStrategy


class NotificationCreator:
    def __init__(self, storage: NotificationStorage, notifier: Notifier):
        self.storage = storage
        self.notifier = notifier

    def create_delayed_notification(self, delay_seconds: int, title: str, message: str):
        data = {
            "type": "delayed",
            "delay_seconds": delay_seconds,
            "title": title,
            "message": message
        }
        self.storage.save_notification(data)

    def create_scheduled_notification(self, datetime_str: str, title: str, message: str):
        data = {
            "type": "scheduled",
            "target_datetime": datetime_str,
            "title": title,
            "message": message
        }
        self.storage.save_notification(data)

    def load_notifications(self) -> list[NotificationStrategy]:
        notifications = []
        for item in self.storage.load_notifications():
            notif_type = item.get("type")
            title = item.get("title")
            message = item.get("message")

            if notif_type == "delayed":
                delay = item.get("delay_seconds", 0)
                scheduled_time = datetime.now() + timedelta(seconds=delay)
                strategy = DelayedNotification(delay, title, message, self.notifier)
                notifications.append((scheduled_time, strategy))

            elif notif_type == "scheduled":
                datetime_str = item.get("target_datetime")
                try:
                    scheduled_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
                    strategy = ScheduledNotification(datetime_str, title, message, self.notifier)
                    notifications.append((scheduled_time, strategy))
                except ValueError:
                    print(f"[ОШИБКА] Пропущено уведомление с неправильной датой: {datetime_str}")

        notifications.sort(key=lambda x: x[0])
        return [strategy for _, strategy in notifications]

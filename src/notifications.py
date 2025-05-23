import time

from abc import ABC, abstractmethod
from plyer import notification
from datetime import datetime, timedelta


class Notifier:
    def show_notification(self, title: str, message: str):
        notification.notify(
            title=title,
            message=message,
            app_name='Уведомлятор',
            timeout=10
        )


class NotificationStrategy(ABC):
    def __init__(self, title: str, message: str, notifier: Notifier):
        self.title = title
        self.message = message
        self.notifier = notifier

    @abstractmethod
    def notify(self):
        pass


class NotificationManager:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def run(self):
        self.strategy.notify()

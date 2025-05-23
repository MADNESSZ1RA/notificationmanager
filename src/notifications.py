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
            timeout=60
        )


class NotificationStrategy(ABC):
    def __init__(self, title: str, message: str, notifier: Notifier):
        self.title = title
        self.message = message
        self.notifier = notifier

    @abstractmethod
    def notify(self):
        pass


class DelayedNotification(NotificationStrategy):
    def __init__(self, delay_seconds: int, title: str, message: str, notifier: Notifier):
        super().__init__(title, message, notifier)
        self.delay_seconds = delay_seconds

    def notify(self):
        print(f"Ожидание {self.delay_seconds} секунд...")
        time.sleep(self.delay_seconds)
        self.notifier.show_notification(self.title, self.message)


class ScheduledNotification(NotificationStrategy):
    def __init__(self, target_datetime: str, title: str, message: str, notifier: Notifier):
        super().__init__(title, message, notifier)
        self.target_datetime = target_datetime

    def notify(self):
        try:
            target = datetime.strptime(self.target_datetime, "%Y-%m-%d %H:%M")
        except ValueError:
            print(
                f"[ОШИБКА] Неверный формат даты/времени: {self.target_datetime}")
            return

        now = datetime.now()
        if target < now:
            print(
                f"[ПРОПУЩЕНО] {self.title} — дата уже прошла: {self.target_datetime}")
            return

        seconds_left = (target - now).total_seconds()

        if seconds_left > 3600 * 24:
            print(
                f"[ПРОПУЩЕНО] {self.title} — слишком далеко: {int(seconds_left // 60)} минут")
            return

        print(f"Ожидание до {self.target_datetime} ({int(seconds_left)} сек.)")
        time.sleep(seconds_left)
        self.notifier.show_notification(self.title, self.message)


class NotificationManager:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy

    def run(self):
        self.strategy.notify()

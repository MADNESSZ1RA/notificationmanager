from PySide6.QtCore import QObject, Slot, QUrl
from src.notification_storage import NotificationStorage
from src.notification_creator import NotificationCreator
from src.notifications import Notifier


class AppBridge(QObject):
    def __init__(self):
        super().__init__()
        self.storage = NotificationStorage()
        self.creator = NotificationCreator(self.storage, Notifier())
        self.view = None

    @Slot(str, str, str)
    def addScheduledNotification(self, time_str, title, message):
        self.creator.create_scheduled_notification(time_str, title, message)

    @Slot(int, str, str)
    def addDelayedNotification(self, delay_seconds, title, message):
        self.creator.create_delayed_notification(delay_seconds, title, message)

    @Slot()
    def openNotificationsPage(self):
        if self.view:
            self.view.load(QUrl.fromLocalFile("ui/pages/notifications.html"))

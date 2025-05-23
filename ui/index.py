import json
import os
import uuid

from datetime import datetime, timedelta

from PySide6.QtWidgets import QWidget, QMainWindow, QMessageBox
from PySide6.QtCore import QTimer, Qt, QDate, QTime

from ui.pages.ui_index import Ui_Index
from src.notification_manager import NotificationStorage
from src.notifications import Notifier


class IndexPage(QWidget, Ui_Index):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.setupUi(self)

        self.main_window = main_window
        self.notifier = Notifier()
        self.timeDateInput.setDate(QDate.currentDate())
        self.timeTimeInput.setTime(QTime.currentTime())
        self.timeTimeInput.setDisplayFormat("HH:mm")

        self.timeAddButton.clicked.connect(self.add_time)
        self.waitAddButton.clicked.connect(self.add_wait)
        self.notificationsListButton.clicked.connect(self.open_list)
        self.radioButton.toggled.connect(self.toggle_notification_watcher)

        self.notification_timer = QTimer(self)
        self.notification_timer.setInterval(0)
        self.notification_timer.setTimerType(Qt.CoarseTimer)
        self.notification_timer.timeout.connect(self.check_notifications)

        self.notified_ids: set[str] = set()

        if self.get_work_status():
            self.radioButton.setChecked(True)
            self.notification_timer.start()

    def get_work_status(self) -> bool:
        if not os.path.exists("notifications.json"):
            return False
        try:
            with open("notifications.json", "r", encoding="utf-8") as f:
                return json.load(f).get("work", False)
        except json.JSONDecodeError:
            return False

    def set_work_status(self, status: bool) -> None:
        data = {}
        if os.path.exists("notifications.json"):
            try:
                with open("notifications.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                pass
        data["work"] = status
        with open("notifications.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def toggle_notification_watcher(self, checked: bool) -> None:
        self.set_work_status(checked)
        if checked:
            self.notification_timer.start()
        else:
            self.notification_timer.stop()

    def check_notifications(self) -> None:
        if not self.get_work_status():
            return

        now = datetime.now()
        start_minute = now.replace(second=0, microsecond=0)
        end_minute = start_minute + timedelta(minutes=1)

        for n in NotificationStorage.load():
            try:
                scheduled = datetime.strptime(n["time"], "%Y-%m-%d %H:%M")
            except ValueError:
                continue

            if start_minute <= scheduled < end_minute:
                notif_id = n["id"]
                if notif_id not in self.notified_ids:
                    self.notifier.show_notification(n["title"], n["message"])
                    NotificationStorage.purge_processed()
                    self.notified_ids.add(notif_id)

    def add_time(self) -> None:
        date_str = self.timeDateInput.date().toString("dd.MM.yyyy")
        time_str = self.timeTimeInput.time().toString("HH:mm")
        title = self.timeTitleInput.text().strip()
        message = self.timeDescriptionInput.text().strip()

        if not (date_str and time_str and title and message):
            QMessageBox.warning(
                self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        try:
            dt = datetime.strptime(f"{date_str} {time_str}", "%d.%m.%Y %H:%M")
        except ValueError:
            QMessageBox.critical(self, "Неверный формат",
                                 "Введите дату в формате ДД.ММ.ГГГГ и время в ЧЧ:ММ")
            return

        NotificationStorage.add({
            "id": str(uuid.uuid4()),
            "type": "Запланированное",
            "time": dt.strftime("%Y-%m-%d %H:%M"),
            "title": title,
            "message": message
        })
        QMessageBox.information(self, "Готово", "Уведомление добавлено!")

    def add_wait(self) -> None:
        delay_text = self.waitTimeInput.text().strip()
        title = self.waitTitleInput.text().strip()
        message = self.waitDescriptionInput.text().strip()

        if not (delay_text and title and message):
            QMessageBox.warning(
                self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        try:
            delay_minutes = int(delay_text)
            dt = datetime.now() + timedelta(minutes=delay_minutes)
        except ValueError:
            QMessageBox.critical(self, "Неверный формат",
                                 "Введите число минут (целое число).")
            return

        NotificationStorage.add({
            "id": str(uuid.uuid4()),
            "type": "С задержкой",
            "time": dt.strftime("%Y-%m-%d %H:%M"),
            "title": title,
            "message": message
        })
        QMessageBox.information(self, "Готово", "Уведомление добавлено!")

    def open_list(self) -> None:
        from ui.notifications_list import NotificationsList
        self.main_window.setCentralWidget(NotificationsList(self.main_window))

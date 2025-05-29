import sys
import os
from pathlib import Path
from PySide6.QtWidgets import (
    QMainWindow, QSystemTrayIcon, QMenu
)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import Qt, QEvent, QTimer


def resource_path(rel_path: str) -> str:
    base_path = getattr(sys, "_MEIPASS", Path(__file__).resolve().parent)
    return os.fspath(Path(base_path, rel_path))



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(550, 250)
        self.setMaximumSize(750, 250)
        self.setWindowTitle("Мастер уведомлений")

        icon = QIcon(resource_path("ui/img/favicon.ico"))

        self.tray = QSystemTrayIcon(icon, self)
        self.tray.setToolTip("Мастер уведомлений")

        menu = QMenu()
        action_show = QAction("Открыть", self)
        action_quit = QAction("Выйти", self)
        menu.addAction(action_show)
        menu.addSeparator()
        menu.addAction(action_quit)

        action_show.triggered.connect(self.restore_from_tray)
        action_quit.triggered.connect(self.quit_app)

        self.tray.setContextMenu(menu)
        self.tray.activated.connect(self.icon_activated)
        self.tray.show()

    def icon_activated(self, reason: QSystemTrayIcon.ActivationReason):
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            self.restore_from_tray()

    def restore_from_tray(self):
        self.showNormal()
        self.raise_()
        self.activateWindow()

    def quit_app(self):
        self.tray.hide()
        self.close()

    def closeEvent(self, event):
        if self.isVisible():
            event.ignore()
            self.hide()
            self.tray.showMessage(
                "Мастер уведомлений",
                "Приложение свернуто в трей.\n"
                "Двойной клик по иконке — вернуть окно.",
                QSystemTrayIcon.Information,
                3000,
            )
        else:
            super().closeEvent(event)

    def changeEvent(self, event):
        if event.type() == QEvent.WindowStateChange:
            if self.windowState() & Qt.WindowMinimized:
                QTimer.singleShot(0, self.hide)
        super().changeEvent(event)

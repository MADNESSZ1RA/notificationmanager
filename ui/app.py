import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from ui.main_window import MainWindow


def run_app():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('resources/icons/master_pol.ico'))
    app.setStyle("windowsvista")

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
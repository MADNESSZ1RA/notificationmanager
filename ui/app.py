import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

from ui.main_window import MainWindow
from ui.index import IndexPage


def run_app():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('ui/img/favicon.ico'))

    main_window = MainWindow()
    main_window.setCentralWidget(IndexPage(main_window))
    main_window.show()

    sys.exit(app.exec())

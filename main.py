import sys

from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon

from variables import WINDOW_ICON_PATH
from main_window import MainWindow
from display import Display

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    # set app icon
    # icon = QIcon(str(WINDOW_ICON_PATH))
    # window.setWindowIcon(icon)
    # app.setWindowIcon(icon)

    # display
    display = Display('My text')
    window.add_widget_to_layout(display)

    window.adjust_fixed_size()
    window.show()
    app.exec()
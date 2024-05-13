from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # layout configuration
        self.cw = QWidget()
        self.wlayout = QVBoxLayout()
        self.cw.setLayout(self.wlayout)
        self.setCentralWidget(self.cw)

        # set title
        self.setWindowTitle('Calculator')

    def adjustFixedSize(self):
        # adjustments for screen size
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

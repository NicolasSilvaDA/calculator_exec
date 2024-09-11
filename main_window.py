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

    def adjust_fixed_size(self) -> None:
        # adjustments for screen size
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def add_widget_to_layout(self, widget: QWidget) -> None:
        self.wlayout.addWidget(widget)
        self.adjust_fixed_size()

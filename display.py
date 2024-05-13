from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

from variables import BIG_FONT, MIN_WIDTH, TEXT_MARGIN

class Display(QLineEdit):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config_style()
        

    def config_style(self) -> None:
        margins = [TEXT_MARGIN for _ in range(4)]

        self.setStyleSheet(f'font-size: {BIG_FONT}px')

        self.setMinimumSize(MIN_WIDTH, (BIG_FONT*2))

        self.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.setTextMargins(*margins)
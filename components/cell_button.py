from enum import Enum

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QPushButton


class Status(Enum):
    VISIBLE = 0
    HIDDEN = 1
    FLAG = 2


class CellButton(QPushButton):
    toggle_flag = pyqtSignal(int, int)

    def __init__(self, row: int, col: int):
        super().__init__()
        self.row = row
        self.col = col
        self.status = Status.HIDDEN
        self.value = 0
        self.bomb = False

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.toggle_flag.emit(self.row, self.col)
        elif e.button() == Qt.MouseButton.LeftButton and self.status == Status.HIDDEN:
            self.status = Status.VISIBLE
            self.render_data()

    def render_data(self):
        if self.status == Status.VISIBLE:
            if self.bomb:
                self.setText("💣")
            else:
                self.setText(str(self.value))
        elif self.status == Status.FLAG:
            self.setText("🚩")
        elif self.status == Status.HIDDEN:
            self.setText("")

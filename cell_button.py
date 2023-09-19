from enum import Enum

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton


class Status(Enum):
    VISIBLE = 0
    HIDDEN = 1
    FLAG = 2


class CellButton(QPushButton):
    def __init__(self, has_flags, add_flag, remove_flag):
        super().__init__()
        self.status = Status.HIDDEN
        self.value = 0
        self.bomb = False
        self.has_flags = has_flags
        self.add_flag = add_flag
        self.remove_flag = remove_flag

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

    def handle_right_click(self):
        if self.status == Status.FLAG:
            self.remove_flag()
            self.status = Status.HIDDEN
            self.render_data()
        elif self.has_flags():
            self.status = Status.FLAG
            self.render_data()
            self.add_flag()

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.RightButton:
            self.handle_right_click()
        elif e.button() == Qt.MouseButton.LeftButton:
            print('Clic izquierdo')

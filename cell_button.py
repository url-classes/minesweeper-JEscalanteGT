from enum import Enum

from PyQt6.QtWidgets import QPushButton


class Status(Enum):
    VISIBLE = 0
    HIDDEN = 1
    FLAG = 2


class CellButton:
    def __init__(self):
        self.status = Status.HIDDEN
        self.value = 0
        self.bomb = False
        self.element = QPushButton()
        self.element.clicked.connect(self.handle_click)

    def render(self):
        if self.status == Status.VISIBLE:
            if self.bomb:
                self.element.setText("💣")
            else:
                self.element.setText(str(self.value))
        elif self.status == Status.FLAG:
            self.element.setText("🚩")
        elif self.status == Status.HIDDEN:
            self.element.setText("")

    def handle_click(self):
        print('Ay!')

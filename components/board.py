import random
from typing import Callable

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QGridLayout

from components import CellButton, CellButtonStatus


class Board(QWidget):
    add_flag = pyqtSignal()
    remove_flag = pyqtSignal()

    def __init__(self, bombs: int, rows: int, cols: int, check_flags_availability: Callable[[], bool]):
        super().__init__()
        self.buttons: list[list[CellButton]] = []
        self.check_flags_availability = check_flags_availability
        self.main_layout = QGridLayout()

        self.create_buttons(rows, cols)
        self.add_bombs(bombs, rows, cols)
        self.add_hints(rows, cols)
        self.setLayout(self.main_layout)

    def add_bombs(self, bombs: int, rows: int, cols: int):
        for i in range(bombs):
            row = random.randint(0, rows - 1)
            col = random.randint(0, cols - 1)
            button = self.buttons[row][col]

            while button.bomb:
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - 1)
                button = self.buttons[row][col]

            button.bomb = True
            button.render_data()

    def add_hints(self, rows: int, cols: int):
        for row in range(rows):
            for col in range(cols):
                button = self.buttons[row][col]
                if not button.bomb:
                    top_left_cell = row == 0 and col == 0
                    top_right_cell = row == 0 and col == cols - 1
                    bottom_left_cell = row == rows - 1 and col == 0
                    bottom_right_cell = row == rows - 1 and col == cols - 1

                    if top_left_cell:
                        button.value = self.visit_corner_cell(0, 0)
                    elif top_right_cell:
                        button.value = self.visit_corner_cell(0, cols - 2)
                    elif bottom_left_cell:
                        button.value = self.visit_corner_cell(rows - 2, 0)
                    elif bottom_right_cell:
                        button.value = self.visit_corner_cell(rows - 2, cols - 2)

    def create_buttons(self, rows: int, cols: int):
        self.main_layout = QGridLayout()

        for row in range(rows):
            new_row: list[CellButton] = []
            for col in range(cols):
                cell_button = CellButton(row, col)
                cell_button.toggle_flag.connect(self.handle_toggle_flag)
                new_row.append(cell_button)
                self.main_layout.addWidget(cell_button, row, col)
            self.buttons.append(new_row)

    def handle_toggle_flag(self, row: int, col: int):
        button = self.buttons[row][col]
        if self.check_flags_availability() and button.status == CellButtonStatus.HIDDEN:
            self.add_flag.emit()
            button.status = CellButtonStatus.FLAG
        elif button.status == CellButtonStatus.FLAG:
            self.remove_flag.emit()
            button.status = CellButtonStatus.HIDDEN
        button.render_data()

    def visit_corner_cell(self, row: int, col: int):
        bombs = 0

        bombs = bombs + 1 if self.buttons[row][col].bomb else bombs + 0
        bombs = bombs + 1 if self.buttons[row][col + 1].bomb else bombs + 0
        bombs = bombs + 1 if self.buttons[row + 1][col + 1].bomb else bombs + 0
        bombs = bombs + 1 if self.buttons[row + 1][col].bomb else bombs + 0

        return bombs

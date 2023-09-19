from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QGridLayout, QPushButton

from cell_button import CellButton


class MainWindow(QMainWindow):
    def __init__(self, cols: int, rows: int, bombs: int):
        super().__init__()
        self.cols = cols
        self.rows = rows
        self.flags = 0
        self.bombs = bombs
        self.setWindowTitle('Buscaminas')

        self.load_ui()

    def load_ui(self):
        central_widget = QWidget()

        main_layout = QVBoxLayout()

        main_layout.addLayout(self.make_score_layout())
        main_layout.addLayout(self.make_board_layout())

        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

    def make_board_layout(self):
        board_layout = QGridLayout()

        for i in range(self.rows):
            for j in range(self.cols):
                cell_button = CellButton(
                    self.has_flags,
                    self.add_flag,
                    self.remove_flag
                )
                cell_button.render_data()
                board_layout.addWidget(cell_button, i, j)

        return board_layout

    def has_flags(self) -> bool:
        return self.flags < self.bombs

    def add_flag(self):
        print(self.flags)
        self.flags += 1

    def remove_flag(self):
        print(self.flags)
        self.flags -= 1

    @staticmethod
    def make_score_layout():
        score_layout = QHBoxLayout()
        label1 = QLabel('SCORE')
        score_layout.addWidget(label1)

        return score_layout

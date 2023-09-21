from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel

from components import Board


class MainWindow(QMainWindow):
    def __init__(self, cols: int, rows: int, bombs: int):
        super().__init__()
        self.cols = cols
        self.rows = rows
        self.flags = 0
        self.bombs = bombs
        self.setWindowTitle('Buscaminas')
        self.board = Board(bombs, rows, cols, self.check_flags_availability)
        self.board.add_flag.connect(self.handle_add_flag)
        self.board.remove_flag.connect(self.handle_remove_flag)
        self.load_ui()

    def check_flags_availability(self) -> bool:
        return self.flags < self.bombs

    def handle_add_flag(self):
        self.flags = min(self.flags + 1, self.bombs)

    def handle_remove_flag(self):
        self.flags = max(self.flags - 1, 0)

    def load_ui(self):
        central_widget = QWidget()

        main_layout = QVBoxLayout()

        main_layout.addLayout(self.make_score_layout())
        main_layout.addWidget(self.board)

        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

    @staticmethod
    def make_score_layout():
        score_layout = QHBoxLayout()
        label1 = QLabel('SCORE')
        score_layout.addWidget(label1)

        return score_layout

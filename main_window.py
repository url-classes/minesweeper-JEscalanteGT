from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QGridLayout, QPushButton

from cell_button import CellButton


class MainWindow(QMainWindow):
    def __init__(self, cols: int, rows: int):
        super().__init__()
        self.cols = cols
        self.rows = rows
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
                cell_button = CellButton()
                cell_button.render()
                board_layout.addWidget(cell_button.element, i, j)

        return board_layout

    @staticmethod
    def make_score_layout():
        score_layout = QHBoxLayout()
        label1 = QLabel('SCORE')
        score_layout.addWidget(label1)

        return score_layout

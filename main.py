import random

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow,\
    QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

from PyQt6.QtGui import QPalette, QColor

import sys

level = 'easy'
rows = 10
cols = 10
bombs = 10
cells = []


def fill_cells():
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)

        cells.append(row)


def create_data():
    fill_cells()
    for i in range(bombs):
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        data = cells[x][y]

        while data == -1:
            x = random.randint(0, cols - 1)
            y = random.randint(0, rows - 1)
            data = cells[x][y]

        cells[x][y] = -1


def calculate_numbers():
    for x in range(0, rows):
        for y in range(0, cols):
            current_cell = cells[x][y]
            if current_cell == -1:
                print('Es una bomba')
            else:
                if (x == 0 and y == 0) or (x == 0 and y == cols - 1) or (x == rows - 1 and y == 0) or (x == rows - 1 and y == cols -1):
                    print('Estoy en una esquina')
                elif x == 0 and (0 < y <= cols - 2):
                    print('Estoy en el borde superior')
                elif y == cols - 1 and (0 < x <= rows - 2):
                    print('Estoy en el borde derecho')
                elif x == rows - 1 and (0 < y <= cols - 2):
                    print('Estoy en el borde inferior')
                elif y == 0 and (0 < x <= rows - 2):
                    print('Estoy en el borde izquierdo')
                else:
                    print('Estoy en el centro')



def make_board_layout():
    board_layout = QGridLayout()

    for i in range(rows):
        for j in range(cols):
            button = QPushButton()
            board_layout.addWidget(button, i, j)

    return board_layout


def make_score_layout():
    score_layout = QHBoxLayout()
    label1 = QLabel('SCORE')
    score_layout.addWidget(label1)

    return score_layout


def main():
    app = QApplication(sys.argv)

    window = QMainWindow()

    window.setWindowTitle('Buscaminas')

    create_data()
    calculate_numbers()

    print(cells)

    main_layout = QVBoxLayout()

    main_layout.addLayout(make_score_layout())
    main_layout.addLayout(make_board_layout())

    central_widget = QWidget()

    central_widget.setLayout(main_layout)

    window.setCentralWidget(central_widget)

    window.show()

    app.exec()


main()

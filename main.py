import random

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow,\
    QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

from PyQt6.QtGui import QPalette, QColor

from main_window import MainWindow

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


def visitar_esquina(x, y):
    sum_bombs = 0

    sum_bombs = sum_bombs + 1 if cells[x][y] == -1 else sum_bombs + 0
    sum_bombs = sum_bombs + 1 if cells[x][y + 1] == -1 else sum_bombs + 0
    sum_bombs = sum_bombs + 1 if cells[x + 1][y + 1] == -1 else sum_bombs + 0
    sum_bombs = sum_bombs + 1 if cells[x + 1][y] == -1 else sum_bombs + 0

    return sum_bombs


def calculate_numbers():
    for x in range(0, rows):
        for y in range(0, cols):
            current_cell = cells[x][y]
            if current_cell == -1:
                print('Es una bomba')
            else:
                superior_izquierda = x == 0 and y == 0
                superior_derecha = x == 0 and y == cols - 1
                inferior_izquierda = x == rows - 1 and y == 0
                inferior_derecha = x == rows - 1 and y == cols - 1

                if superior_izquierda:
                    cells[0][0] = visitar_esquina(0, 0)
                elif superior_derecha:
                    cells[0][cols - 1] = visitar_esquina(0, cols - 2)
                elif inferior_derecha:
                    cells[rows - 1][cols - 1] = visitar_esquina(rows - 2, cols - 2)
                elif inferior_izquierda:
                    cells[rows - 1][0] = visitar_esquina(rows - 2, 0)

                '''
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
                '''


def main():
    app = QApplication(sys.argv)

    window = MainWindow(cols, rows, bombs)

    create_data()
    calculate_numbers()

    window.show()

    app.exec()


main()

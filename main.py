from PyQt6.QtWidgets import QApplication
import sys

from windows import MainWindow

level = 'easy'
rows = 10
cols = 10
bombs = 10
cells = []


def main():
    app = QApplication(sys.argv)

    window = MainWindow(cols, rows, bombs)

    window.show()

    app.exec()


main()

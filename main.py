from window import Window
from cell import Cell


def main():
    window = Window(800, 600)
    cell1 = Cell(window)
    cell2 = Cell(window)
    cell1.has_bottom_wall = False
    cell1.draw(100, 200, 300, 400)
    cell2.has_right_wall = False
    cell2.draw(500, 600, 400, 500)
    window.wait_for_close()


main()

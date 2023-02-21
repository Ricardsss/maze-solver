from window import Window, Line, Point


def main():
    window = Window(800, 600)
    line = Line(Point(20, 40), Point(200, 400))
    window.draw_line(line, "black")
    window.wait_for_close()


main()

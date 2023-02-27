from cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows -
                                        1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while 1:
            need_to_visit = []
            if i + 1 < self._num_cols:
                if not self._cells[i + 1][j].visited:
                    need_to_visit.append([i + 1, j, "right"])
            if i - 1 >= 0:
                if not self._cells[i - 1][j].visited:
                    need_to_visit.append([i - 1, j, "left"])
            if j + 1 < self._num_rows:
                if not self._cells[i][j + 1].visited:
                    need_to_visit.append([i, j + 1, "down"])
            if j - 1 >= 0:
                if not self._cells[i][j - 1].visited:
                    need_to_visit.append([i, j - 1, "up"])
            if len(need_to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                direction = random.choice(need_to_visit)
                if direction[2] == "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[i + 1][j].has_left_wall = False
                elif direction[2] == "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[i - 1][j].has_right_wall = False
                elif direction[2] == "down":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j + 1].has_top_wall = False
                elif direction[2] == "up":
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j - 1].has_bottom_wall = False
                self._break_walls_r(direction[0], direction[1])

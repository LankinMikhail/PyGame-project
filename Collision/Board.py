import pygame
from Collision.Border import Border


class Board:
    def __init__(self, width, height):
        self.left = None
        self.top = None
        self.cell_size = None
        self.width = width
        self.height = height
        self.board = [[""] * width for _ in range(height)]
        self.set_default()

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def set_default(self):
        for j in range(self.width):
            for i in range(self.height):
                self.board[i][j] = ""
        for i in range(self.width):
            self.board[0][i] += "U"
            self.board[-1][i] += "D"
        for i in range(self.height):
            self.board[i][0] += "L"
            self.board[i][-1] += "R"

    def edge(self, i, j, s):
        if s == "U":
            st = (self.top + j * self.cell_size - 1, self.left + i * self.cell_size)
            end = (self.top + (j + 1) * self.cell_size + 1, self.left + i * self.cell_size)
        elif s == "L":
            st = (self.top + j * self.cell_size, self.left + i * self.cell_size - 1)
            end = (self.top + j * self.cell_size, self.left + (i + 1) * self.cell_size + 1)
        elif s == "D":
            st = (self.top + j * self.cell_size - 1, self.left + (i + 1) * self.cell_size)
            end = (self.top + (j + 1) * self.cell_size + 1, self.left + (i + 1) * self.cell_size)
        elif s == "R":
            st = (self.top + (j + 1) * self.cell_size, self.left + i * self.cell_size - 1)
            end = (self.top + (j + 1) * self.cell_size, self.left + (i + 1) * self.cell_size + 1)
        return st, end

    def fill(self, level):
        for j in range(self.width):
            for i in range(self.height):
                self.board[i][j] += level[i][j]
        for j in range(self.width):
            for i in range(self.height):
                for s in self.board[i][j]:
                    if s == "U" or s == "D":
                        st, end = self.edge(i, j, s)
                        Border(st[0], st[1] + 3, end[0], end[1] + 3)
                        Border(st[0], st[1] - 3, end[0], end[1] - 3)
                        Border(st[0], st[1] - 3, st[0], st[1] + 3)
                        Border(end[0], end[1] - 3, end[0], end[1] + 3)
                    elif s == "L" or s == "R":
                        st, end = self.edge(i, j, s)
                        Border(st[0] + 3, st[1], end[0] + 3, end[1])
                        Border(st[0] - 3, st[1], end[0] - 3, end[1])
                        Border(st[0] - 3, st[1], st[0] + 3, st[1])
                        Border(end[0] - 3, end[1], end[0] + 3, end[1])

    def render(self, screen):
        for j in range(self.width):
            for i in range(self.height):
                for s in self.board[i][j]:
                    st, end = self.edge(i, j, s)
                    pygame.draw.line(screen, "black", st, end, 5)

    def get_cell(self, coords):
        if coords[0] < self.left or coords[1] < self.top or (
                coords[0] > self.left + self.height * self.cell_size) or (
                coords[1] > self.top + self.width * self.cell_size):
            return None
        cell = [0, 0]
        cell[0] = (coords[0] - self.left) // self.cell_size
        cell[1] = (coords[1] - self.top) // self.cell_size
        return tuple(cell)

    def on_click(self, cell):
        pass

    def get_click(self, coords):
        cell = self.get_cell(coords)
        self.on_click(cell)
        return cell

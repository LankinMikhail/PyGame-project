import pygame
from pygame import gfxdraw
import sys
import random


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

    def fill(self, level):
        for j in range(self.width):
            for i in range(self.height):
                self.board[i][j] += level[i][j]

    def render(self, screen):
        for j in range(self.width):
            for i in range(self.height):
                if "U" in self.board[i][j]:
                    pygame.draw.line(screen, "black",
                                     (self.top + j * self.cell_size, self.left + i * self.cell_size),
                                     (self.top + (j + 1) * self.cell_size, self.left + i * self.cell_size),
                                     3)
                if "L" in self.board[i][j]:
                    pygame.draw.line(screen, "black",
                                     (self.top + j * self.cell_size, self.left + i * self.cell_size),
                                     (self.top + j * self.cell_size, self.left + (i + 1) * self.cell_size),
                                     3)
                if "D" in self.board[i][j]:
                    pygame.draw.line(screen, "black",
                                     (self.top + j * self.cell_size, self.left + (i + 1) * self.cell_size),
                                     (self.top + (j + 1) * self.cell_size, self.left + (i + 1) * self.cell_size),
                                     3)
                if "R" in self.board[i][j]:
                    pygame.draw.line(screen, "black",
                                     (self.top + (j + 1) * self.cell_size, self.left + i * self.cell_size),
                                     (self.top + (j + 1) * self.cell_size, self.left + (i + 1) * self.cell_size),
                                     3)

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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, vx, vy):
        super().__init__()
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def render(self, screen):
        gfxdraw.aacircle(screen, self.x, self.y, self.radius, (0, 0, 0))
        gfxdraw.filled_circle(screen, self.x, self.y, self.radius, (0, 0, 0))


class Border(pygame.sprite.Sprite):
    def __init__(self):
        pass


level1 = [["", "", "", "", "", "", "", "", "", "", ""],
          ["", "RLU", "", "", "", "", "", "", "", "", ""],
          ["", "LD", "UD", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "UR", "U", "LU", "", "", ""],
          ["", "", "", "", "", "D", "D", "DR", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", ""]]
FPS = 60
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    running = True
    field = Board(11, 9)
    field.set_view(10, 10, 80)
    field.fill(level1)
    bullets = [Bullet(3, 200, 200, 3, 3)]
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((230, 230, 230))
        field.render(screen)
        for bullet in bullets:
            bullet.render(screen)
            bullet.update()
        clock.tick(FPS)
        pygame.display.flip()

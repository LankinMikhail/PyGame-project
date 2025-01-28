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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, vx, vy, life):
        super().__init__()
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = life

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        if self.life == 0:
            bullets.remove(self)
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        elif pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx

    def render(self, screen):
        gfxdraw.aacircle(screen, self.x, self.y, self.radius, (0, 0, 0))
        gfxdraw.filled_circle(screen, self.x, self.y, self.radius, (0, 0, 0))


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if x1 == x2:
            self.add(vertical_borders)
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

    def render(self, screen):
        if self.x1 == self.x2:
            pygame.draw.rect(screen, "green", self.rect)
        else:
            pygame.draw.rect(screen, "red", self.rect)


level1 = [["", "", "", "", "", "", "", "", "", "", ""],
          ["", "RLU", "", "", "", "", "", "", "", "", ""],
          ["", "LD", "UD", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", ""],
          ["", "", "", "", "", "U", "", "LU", "", "", ""],
          ["", "", "", "", "", "D", "D", "DR", "", "", ""],
          ["", "", "", "", "", "", "", "", "", "", ""]]
FPS = 120
if __name__ == "__main__":
    pygame.init()
    screenbase = pygame.display.set_mode((2000, 1600))
    screen = pygame.transform.scale(screenbase, (1000, 800))
    running = True
    horizontal_borders = pygame.sprite.Group()
    vertical_borders = pygame.sprite.Group()
    field = Board(11, 9)
    field.set_view(10, 10, 80)
    field.fill(level1)
    bullets = []
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullets.append(Bullet(3, event.pos[0], event.pos[1], 1, 1, 2400))
        screen.fill((230, 230, 230))
        field.render(screen)
        for bullet in bullets:
            bullet.render(screen)
            bullet.update()
        for border in horizontal_borders:
            pass
            #border.render(screen)
        for border in vertical_borders:
            pass
            #border.render(screen)
        clock.tick(FPS)
        pygame.display.flip()

import pygame
import sys
import random


class Board:
    def __init__(self, width, height):
        self.left = None
        self.top = None
        self.cell_size = None
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.move = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        pass

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


FPS = 30
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("white")
        pygame.display.flip()

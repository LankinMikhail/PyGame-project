import pygame
from Collision.Board import Board
from Collision.Bullet import Bullet, bullets
from Collision.Border import horizontal_borders, vertical_borders
import sys
import random


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
    screen = pygame.display.set_mode((1000, 800))
    running = True
    field = Board(11, 9)
    field.set_view(10, 10, 80)
    field.fill(level1)
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

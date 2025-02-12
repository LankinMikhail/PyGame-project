import pygame
from Collision.Board import Board
from Collision.Bullet import Bullet, bullets
from Collision.Border import horizontal_borders, vertical_borders
from Collision.Player import Player
import sys
import os
import random
import math


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
    screen = pygame.display.set_mode((1120, 920))
    running = True
    field = Board(11, 9)
    field.set_view(10, 10, 100)
    field.fill(level1)
    clock = pygame.time.Clock()
    player1 = Player(0, 700, 700, 60)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                angle = random.randint(0, 90)
                velocity = 180 / FPS
                bullets.append(Bullet(3, event.pos[0], event.pos[1], velocity * math.sin(math.radians(angle)),
                                      velocity * math.cos(math.radians(angle)), FPS * 30))
            if event.type == pygame.KEYDOWN:
                if event.unicode == "w":
                    player1.motion = "forward"
                if event.unicode == "s":
                    player1.motion = "back"
                if event.unicode == "q":
                    player1.rotating = "left"
                if event.unicode == "e":
                    player1.rotating = "right"
            if event.type == pygame.KEYUP:
                if event.unicode == "w" and player1.motion == "forward":
                    player1.motion = "stop"
                if event.unicode == "s" and player1.motion == "back":
                    player1.motion = "stop"
                if event.unicode == "q" and player1.rotating == "left":
                    player1.rotating = "stop"
                if event.unicode == "e" and player1.rotating == "right":
                    player1.rotating = "stop"
        screen.fill((230, 230, 230))
        field.render(screen)
        player1.render(screen)
        player1.update()
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

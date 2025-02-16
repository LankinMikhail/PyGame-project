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
    players = [Player(1, 700, 700, 0)]
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
                for player in players:
                    if event.unicode == player.w:
                        player.motion = "forward"
                    if event.unicode == player.s:
                        player.motion = "back"
                    if event.unicode == player.d:
                        player.rotating = "left"
                    if event.unicode == player.a:
                        player.rotating = "right"
                    if event.unicode == player.q:
                        bullets.append(player.shoot(FPS))
            if event.type == pygame.KEYUP:
                for player in players:
                    if event.unicode == player.w and player.motion == "forward":
                        player.motion = "stop"
                    if event.unicode == player.s and player.motion == "back":
                        player.motion = "stop"
                    if event.unicode == player.d and player.rotating == "left":
                        player.rotating = "stop"
                    if event.unicode == player.a and player.rotating == "right":
                        player.rotating = "stop"
        screen.fill((230, 230, 230))
        field.render(screen)
        for player in players:
            player.render(screen)
            player.update()
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

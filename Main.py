import pygame
import random
import math
from Collision.Board import Board
from Collision.Bullet import Bullet, bullets, players
from Collision.Player import Player


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
    Player(1, 500, 500, 0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                angle = random.randint(45, 45)
                velocity = 180 / FPS
                bullets.append(Bullet(3, event.pos[0], event.pos[1], velocity * math.sin(math.radians(angle)),
                                      velocity * math.cos(math.radians(angle)), FPS * 30))
            if event.type == pygame.KEYDOWN:
                for player in players:
                    if event.unicode == player.w and player.motion != "no forward":
                        player.motion = "forward"
                    if event.unicode == player.s and player.motion != "no back":
                        player.motion = "back"
                    if event.unicode == player.d and player.rotation != "no left":
                        player.rotation = "left"
                    if event.unicode == player.a and player.rotation != "no right":
                        player.rotation = "right"
                    if event.unicode == player.q:
                        bullets.append(player.shoot(FPS))
            if event.type == pygame.KEYUP:
                for player in players:
                    if event.unicode == player.w and player.motion == "forward":
                        player.motion = "stop"
                    if event.unicode == player.s and player.motion == "back":
                        player.motion = "stop"
                    if event.unicode == player.d and player.rotation == "left":
                        player.rotation = "stop"
                    if event.unicode == player.a and player.rotation == "right":
                        player.rotation = "stop"
        screen.fill((230, 230, 230))
        field.render(screen)
        for bullet in bullets:
            bullet.render(screen)
            bullet.update()
        for player in players:
            player.render(screen)
            player.update()
        clock.tick(FPS)
        pygame.display.flip()

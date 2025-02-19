import pygame
import random
import math
from Collision.Board import Board
from Collision.Bullet import Bullet, bullets, players
from Collision.Player import Player
from Logic.menu import start_screen, second_screen
from Logic.generator import generation, random_place

FPS = 120
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    start = start_screen(screen)
    clock = pygame.time.Clock()
    if start:
        game_mode = second_screen(screen)
    if game_mode[1] == "small":
        width = 6
        height = 5
    elif game_mode[1] == "medium":
        width = 8
        height = 7
    else:
        width = 11
        height = 9
    field = Board(width, height)
    field.set_view(10, 10, 80)
    level = generation(width, height)
    field.fill(level)
    if game_mode[0] == "2":
        already = []
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(1, pos[0], pos[1], pos[2], 1)
        already.append((pos[0], pos[1]))
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(2, pos[0], pos[1], pos[2], 2)
    elif game_mode[0] == "3":
        already = []
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(1, pos[0], pos[1], pos[2], 1)
        already.append((pos[0], pos[1]))
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(2, pos[0], pos[1], pos[2], 2)
        already.append((pos[0], pos[1]))
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(3, pos[0], pos[1], pos[2], 3)
    elif game_mode[0] == "4":
        already = []
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(1, pos[0], pos[1], pos[2], 1)
        already.append((pos[0], pos[1]))
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(2, pos[0], pos[1], pos[2], 2)
        already.append((pos[0], pos[1]))
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(3, pos[0], pos[1], pos[2], 3)
        already.append((pos[0], pos[1]))
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(4, pos[0], pos[1], pos[2], 4)
    else:
        already = []
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(1, pos[0], pos[1], pos[2], 1)
        already.append((pos[0], pos[1]))
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(1, pos[0], pos[1], pos[2], 2)
        already.append((pos[0], pos[1]))
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(4, pos[0], pos[1], pos[2], 3)
        already.append((pos[0], pos[1]))
        pos = random_place(width, height, field.cell_size, field.left, field.top, already)
        Player(4, pos[0], pos[1], pos[2], 4)
    running = True
    for player in players:
        player.render(screen)
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
                    if event.key == player.w and player.motion != "no forward":
                        player.motion = "forward"
                    if event.key == player.s and player.motion != "no back":
                        player.motion = "back"
                    if event.key == player.d and player.rotation != "no left":
                        player.rotation = "left"
                    if event.key == player.a and player.rotation != "no right":
                        player.rotation = "right"
                    if event.key == player.q:
                        bullets.append(player.shoot(FPS))
            if event.type == pygame.KEYUP:
                for player in players:
                    if event.key == player.w and player.motion == "forward":
                        player.motion = "stop"
                    if event.key == player.s and player.motion == "back":
                        player.motion = "stop"
                    if event.key == player.d and player.rotation == "left":
                        player.rotation = "stop"
                    if event.key == player.a and player.rotation == "right":
                        player.rotation = "stop"
        screen.fill((230, 230, 230))
        field.render(screen)
        for bullet in bullets:
            bullet.render(screen)
            bullet.update()
        for player in players:
            if player.is_alive:
                player.render(screen)
                player.update()
        clock.tick(FPS)
        pygame.display.flip()

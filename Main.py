import pygame
from Collision.Board import Board
from Collision.Bullet import bullets, players
from Logic.menu import start_screen, second_screen
from Logic.generator import generation, random_map

FPS = 120
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    start = start_screen(screen)
    clock = pygame.time.Clock()
    game_mode = second_screen(screen)
    running = True
    wait = 0
    scores = [0, 0, 0, 0]
    live = set()
    while running:
        if wait == 0:
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
            random_map(game_mode[0], field)
            wait = FPS * 5
            for player in players:
                player.render(screen)
            for elem in live:
                scores[elem - 1] += 1
            print(scores)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
        live = set()
        for player in players:
            if player.is_alive:
                live.add(player.team)
                player.render(screen)
                player.update()
        if len(live) <= 1:
            wait -= 1
        clock.tick(FPS)
        pygame.display.flip()

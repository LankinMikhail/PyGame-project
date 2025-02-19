import pygame
from Collision.Board import Board
from Collision.Bullet import bullets, players
from Logic.menu import start_screen, second_screen
from Logic.generator import generation, random_map


def score(scores, game_mode, screen):
    f1 = pygame.font.SysFont('Times New Roman', 40)
    f2 = pygame.font.SysFont('Times New Roman', 40)
    f3 = pygame.font.SysFont('Times New Roman', 40)
    f4 = pygame.font.SysFont('Times New Roman', 40)
    tank1 = pygame.image.load("Assets\\счет_танк1.PNG")
    tank2 = pygame.image.load("Assets\\счет_танк2.PNG")
    tank3 = pygame.image.load("Assets\\счет_танк3.PNG")
    tank4 = pygame.image.load("Assets\\счет_танк4.PNG")
    text1 = f1.render(f"{scores[0]}", False, (0, 0, 0))
    text2 = f2.render(f"{scores[1]}", False, (0, 0, 0))
    text3 = f3.render(f"{scores[2]}", False, (0, 0, 0))
    text4 = f4.render(f"{scores[3]}", False, (0, 0, 0))
    if game_mode[0] == "2":
        pos_t1 = (200, 890)
        pos_t2 = (600, 890)
        pos_text1 = (390, 860)
        pos_text2 = (790, 860)
        print(1)
        screen.blit(text1, pos_text1)
        screen.blit(text2, pos_text2)
        screen.blit(tank1, pos_t1)
        screen.blit(tank2, pos_t2)
    elif game_mode[0] == "3":
        pos_t1 = (100, 890)
        pos_t2 = (400, 890)
        pos_t3 = (700, 890)
        pos_text1 = (280, 860)
        pos_text2 = (580, 860)
        pos_text3 = (880, 860)
        screen.blit(text1, pos_text1)
        screen.blit(text2, pos_text2)
        screen.blit(text3, pos_text3)
        screen.blit(tank1, pos_t1)
        screen.blit(tank2, pos_t2)
        screen.blit(tank3, pos_t3)
    else:
        pos_t1 = (40, 890)
        pos_t2 = (280, 890)
        pos_t3 = (520, 890)
        pos_t4 = (760, 890)
        pos_text1 = (220, 860)
        pos_text2 = (560, 860)
        pos_text3 = (700, 860)
        pos_text4 = (940, 860)
        if game_mode[0] == "4":
            screen.blit(tank1, pos_t1)
            screen.blit(tank2, pos_t2)
            screen.blit(tank3, pos_t3)
            screen.blit(tank4, pos_t4)
            screen.blit(text1, pos_text1)
            screen.blit(text2, pos_text2)
            screen.blit(text3, pos_text3)
            screen.blit(text4, pos_text4)
        else:
            screen.blit(tank1, pos_t1)
            screen.blit(tank1, pos_t2)
            screen.blit(tank4, pos_t3)
            screen.blit(tank4, pos_t4)
            text2 = text1
            text3 = text4
            screen.blit(text1, pos_text1)
            screen.blit(text2, pos_text2)
            screen.blit(text3, pos_text3)
            screen.blit(text4, pos_text4)


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
        score(scores, game_mode, screen)
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

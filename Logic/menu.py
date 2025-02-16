import pygame
import sys
import os

from pygame import MOUSEMOTION
from Collision.Bullet import load_image

FPS = 120


def terminate():
    pygame.quit()
    sys.exit()


def fourty_screen(cnt):
    fr_screen = pygame.display.set_mode((1000, 800))
    screen.blit(fr_screen, (0, 0))
    back_button = (0, 725, 140, 800)
    way = os.path.dirname(__file__)[:-6] + "/Assets/"
    anim1_deactivate = [load_image(way + 'im11.PNG'), load_image(way + "im12.PNG")]
    anim2_deactivate = [load_image(way + "im21.PNG"), load_image(way + "im22.PNG")]
    anim3_deactivate = [load_image(way + "im31.PNG"), load_image(way + "im32.PNG")]
    anim4_deactivate = [load_image(way + "im41.PNG"), load_image(way + "im42.PNG")]
    anim1_activate = [load_image(way + "im13.PNG")]
    anim2_activate = [load_image(way + "im23.PNG")]
    anim3_activate = [load_image(way + "im33.PNG")]
    anim4_activate = [load_image(way + "im43.PNG")]
    anim2_activate_2x2 = [load_image(way + "im24.PNG")]
    anim3_activate_2x2 = [load_image(way + "im34.PNG")]
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    flag5 = False
    flag = False
    anim1 = anim1_deactivate
    anim2 = anim2_deactivate
    anim3 = anim3_deactivate
    anim4 = anim4_deactivate
    if cnt == "2x2":
        cnt = "4"
        flag = True
    i = 0
    f = False
    while True:
        fr_screen.fill((225, 225, 225))
        bc_f = pygame.font.SysFont('Times New Roman', 55)
        bc_text = bc_f.render("Back", False, (0, 0, 0))
        bc_pos = (10, 735)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == 113:
                flag1 = not flag1
                if flag1:
                    anim1 = anim1_activate
            if event.type == pygame.KEYDOWN and event.key == 121:
                flag2 = not flag2
                if flag2 and not flag:
                    anim2 = anim2_activate
                elif flag2 and flag:
                    anim2 = anim2_activate_2x2
            if event.type == pygame.KEYDOWN and (event.key == 1073742048 or event.key == 1073742052):
                flag3 = not flag3
                if flag3 and not flag:
                    anim3 = anim3_activate
                elif flag3 and flag:
                    anim3 = anim3_activate_2x2
            if event.type == pygame.KEYDOWN and (event.key == 1073741922 or event.key == 48):
                flag4 = not flag4
                if flag4:
                    anim4 = anim4_activate
            if event.type == MOUSEMOTION and (
                    back_button[0] <= event.pos[0] <= back_button[2] and
                    back_button[1] <= event.pos[1] <= back_button[3]):
                flag5 = True

            elif event.type == MOUSEMOTION and not (
                    back_button[0] <= event.pos[0] <= back_button[2] and
                    back_button[1] <= event.pos[1] <= back_button[3]):
                flag5 = False
            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (back_button[0] <= event.pos[0] <= back_button[2] and
                   back_button[1] <= event.pos[1] <= back_button[3])):
                return False
            if int(cnt) == 2 and flag1 and flag2:
                f = True
            elif int(cnt) == 3 and flag1 and flag2 and flag3:
                f = True
            elif int(cnt) == 4 and flag1 and flag2 and flag3 and flag4:
                f = True
        if cnt == "2":
            anim1_pos = (240, 450)
            anim2_pos = (620, 450)
            fr_screen.blit(anim1[i % len(anim1)], anim1_pos)
            fr_screen.blit(anim2[i % len(anim2)], anim2_pos)
        if cnt == "3":
            anim1_pos = (145, 450)
            anim2_pos = (430, 450)
            anim3_pos = (715, 450)
            fr_screen.blit(anim1[i % len(anim1)], anim1_pos)
            fr_screen.blit(anim2[i % len(anim2)], anim2_pos)
            fr_screen.blit(anim3[i % len(anim3)], anim3_pos)
        if cnt == "4":
            anim1_pos = (88, 450)
            anim2_pos = (316, 450)
            anim3_pos = (544, 450)
            anim4_pos = (772, 450)
            fr_screen.blit(anim1[i % len(anim1)], anim1_pos)
            fr_screen.blit(anim2[i % len(anim2)], anim2_pos)
            fr_screen.blit(anim3[i % len(anim3)], anim3_pos)
            fr_screen.blit(anim4[i % len(anim4)], anim4_pos)
        if flag5:
            bc_f = pygame.font.SysFont('Times New Roman', 75)
            bc_text = bc_f.render("Back", False, (0, 0, 0))
            bc_pos = (0, 725)
        fr_screen.blit(bc_text, bc_pos)
        i += 1
        if i == FPS:
            i = 0
        pygame.display.flip()
        if f:
            pygame.time.wait(500)
            return True
        clock.tick(FPS // 30)


def third_screen(cnt):
    th_screen = pygame.display.set_mode((1000, 800))
    screen.blit(th_screen, (0, 0))
    small_level = (50, 350, 350, 500)
    medium_level = (350, 350, 650, 500)
    large_level = (650, 350, 950, 500)
    back_button = (360, 490, 580, 615)
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    while True:
        th_screen.fill((225, 225, 225))
        sm_f = pygame.font.SysFont('Times New Roman', 60)
        md_f = pygame.font.SysFont('Times New Roman', 60)
        lr_f = pygame.font.SysFont('Times New Roman', 60)
        bc_f = pygame.font.SysFont('Times New Roman', 60)
        sm_text = sm_f.render("     Small", False, (0, 0, 0))
        md_text = md_f.render(" Medium", False, (0, 0, 0))
        lr_text = lr_f.render(" Large", False, (0, 0, 0))
        bc_text = bc_f.render(" Back", False, (0, 0, 0))
        sm_pos_text = (80, 385)
        md_pos_text = (380, 385)
        lr_pos_text = (680, 385)
        bc_pos_text = (410, 510)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION and (
                    small_level[0] <= event.pos[0] <= small_level[2] and
                    small_level[1] <= event.pos[1] <= small_level[3]):
                flag1 = True

            elif event.type == MOUSEMOTION and not (
                    small_level[0] <= event.pos[0] <= small_level[2] and
                    small_level[1] <= event.pos[1] <= small_level[3]):
                flag1 = False

            if event.type == MOUSEMOTION and (
                    medium_level[0] <= event.pos[0] <= medium_level[2] and
                    medium_level[1] <= event.pos[1] <= medium_level[3]):
                flag2 = True

            elif event.type == MOUSEMOTION and not (
                    medium_level[0] <= event.pos[0] <= medium_level[2] and
                    medium_level[1] <= event.pos[1] <= medium_level[3]):
                flag2 = False

            if event.type == MOUSEMOTION and (
                    large_level[0] <= event.pos[0] <= large_level[2] and
                    large_level[1] <= event.pos[1] <= large_level[3]):
                flag3 = True

            elif event.type == MOUSEMOTION and not (
                    large_level[0] <= event.pos[0] <= large_level[2] and
                    large_level[1] <= event.pos[1] <= large_level[3]):
                flag3 = False

            if event.type == MOUSEMOTION and (
                    back_button[0] <= event.pos[0] <= back_button[2] and
                    back_button[1] <= event.pos[1] <= back_button[3]):
                flag4 = True

            elif event.type == MOUSEMOTION and not (
                    back_button[0] <= event.pos[0] <= back_button[2] and
                    back_button[1] <= event.pos[1] <= back_button[3]):
                flag4 = False

            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (small_level[0] <= event.pos[0] <= small_level[2] and
                   small_level[1] <= event.pos[1] <= small_level[3])):
                ans = fourty_screen(cnt)
                if ans:
                    return "small"
            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (medium_level[0] <= event.pos[0] <= medium_level[2] and
                   medium_level[1] <= event.pos[1] <= medium_level[3])):
                ans = fourty_screen(cnt)
                if ans:
                    return "medium"
            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (large_level[0] <= event.pos[0] <= large_level[2] and
                   large_level[1] <= event.pos[1] <= large_level[3])):
                ans = fourty_screen(cnt)
                if ans:
                    return "large"
            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (back_button[0] <= event.pos[0] <= back_button[2] and
                   back_button[1] <= event.pos[1] <= back_button[3])):
                return "back"
        if flag1:
            sm_f = pygame.font.SysFont('Times New Roman', 70)
            sm_text = sm_f.render("     Small", False, (0, 0, 0))
            sm_pos_text = (60, 370)
        elif flag2:
            md_f = pygame.font.SysFont('Times New Roman', 70)
            md_text = md_f.render(" Medium", False, (0, 0, 0))
            md_pos_text = (360, 370)
        elif flag3:
            lr_f = pygame.font.SysFont('Times New Roman', 70)
            lr_text = lr_f.render(" Large", False, (0, 0, 0))
            lr_pos_text = (660, 370)
        elif flag4:
            bc_f = pygame.font.SysFont('Times New Roman', 70)
            bc_text = bc_f.render(" Back", False, (0, 0, 0))
            bc_pos_text = (395, 500)
        th_screen.blit(sm_text, sm_pos_text)
        th_screen.blit(md_text, md_pos_text)
        th_screen.blit(lr_text, lr_pos_text)
        th_screen.blit(bc_text, bc_pos_text)
        pygame.display.flip()
        clock.tick(FPS)


def second_screen():
    sec_screen = pygame.display.set_mode((1000, 800))
    screen.blit(sec_screen, (0, 0))
    mode_button2 = (25, 380, 255, 490)
    mode_button3 = (250, 380, 475, 490)
    mode_button4 = (475, 380, 700, 490)
    mode_button2x2 = (700, 380, 925, 490)
    quit_button = (360, 490, 580, 615)
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    flag5 = False
    while True:
        sec_screen.fill((225, 225, 225))
        f1 = pygame.font.SysFont('Times New Roman', 50)
        f2 = pygame.font.SysFont('Times New Roman', 50)
        f3 = pygame.font.SysFont('Times New Roman', 50)
        f4 = pygame.font.SysFont('Times New Roman', 50)
        f5 = pygame.font.SysFont('Times New Roman', 70)
        text1 = f1.render("2 Player", False, (0, 0, 0))
        text2 = f2.render("3 Player", False, (0, 0, 0))
        text3 = f3.render("4 Player", False, (0, 0, 0))
        text4 = f4.render("2x2 Player", False, (0, 0, 0))
        text5 = f5.render("Quit", False, (0, 0, 0))
        pos_text1 = (55, 405)
        pos_text2 = (280, 405)
        pos_text3 = (505, 405)
        pos_text4 = (730, 405)
        pos_text5 = (410, 510)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION and (
                    mode_button2[0] <= event.pos[0] <= mode_button2[2] and mode_button2[1] <= event.pos[1] <=
                    mode_button2[3]):
                flag1 = True

            elif event.type == MOUSEMOTION and not (
                    mode_button2[0] <= event.pos[0] <= mode_button2[2] and mode_button2[1] <= event.pos[1] <=
                    mode_button2[3]):
                flag1 = False

            if event.type == MOUSEMOTION and (
                    mode_button3[0] <= event.pos[0] <= mode_button3[2] and mode_button3[1] <= event.pos[1] <=
                    mode_button3[3]):
                flag2 = True

            elif event.type == MOUSEMOTION and not (
                    mode_button3[0] <= event.pos[0] <= mode_button3[2] and mode_button3[1] <= event.pos[1] <=
                    mode_button3[3]):
                flag2 = False

            if event.type == MOUSEMOTION and (
                    mode_button4[0] <= event.pos[0] <= mode_button4[2] and mode_button4[1] <= event.pos[1] <=
                    mode_button4[3]):
                flag3 = True

            elif event.type == MOUSEMOTION and not (
                    mode_button4[0] <= event.pos[0] <= mode_button4[2] and mode_button4[1] <= event.pos[1] <=
                    mode_button4[3]):
                flag3 = False

            if event.type == MOUSEMOTION and (
                    mode_button2x2[0] <= event.pos[0] <= mode_button2x2[2] and mode_button2x2[1] <= event.pos[1] <=
                    mode_button2x2[3]):
                flag4 = True

            elif event.type == MOUSEMOTION and not (
                    mode_button2x2[0] <= event.pos[0] <= mode_button2x2[2] and mode_button2x2[1] <= event.pos[1] <=
                    mode_button2x2[3]):
                flag4 = False

            if event.type == MOUSEMOTION and (
                    quit_button[0] <= event.pos[0] <= quit_button[2] and
                    quit_button[1] <= event.pos[1] <= quit_button[3]):
                flag5 = True

            elif event.type == MOUSEMOTION and not (
                    quit_button[0] <= event.pos[0] <= quit_button[2] and
                    quit_button[1] <= event.pos[1] <= quit_button[3]):
                flag5 = False

            if event.type == pygame.QUIT:
                terminate()

            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (mode_button2[0] <= event.pos[0] <= mode_button2[2] and
                   mode_button2[1] <= event.pos[1] <= mode_button2[3])):
                ans = third_screen("2")
                if ans != "back":
                    return ["2", ans]

            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (mode_button3[0] <= event.pos[0] <= mode_button3[2] and
                   mode_button3[1] <= event.pos[1] <= mode_button3[3])):
                ans = third_screen("3")
                if ans != "back":
                    return ["3", ans]

            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (mode_button4[0] <= event.pos[0] <= mode_button4[2] and
                   mode_button4[1] <= event.pos[1] <= mode_button4[3])):
                ans = third_screen("4")
                if ans != "back":
                    return ["4", ans]

            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (mode_button2x2[0] <= event.pos[0] <= mode_button2x2[2] and
                   mode_button2x2[1] <= event.pos[1] <= mode_button2x2[3])):
                ans = third_screen("2x2")
                if ans != "back":
                    return ["2x2", ans]

            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (quit_button[0] <= event.pos[0] <= quit_button[2] and
                   quit_button[1] <= event.pos[1] <= quit_button[3])):
                terminate()
        if flag1:
            f1 = pygame.font.SysFont('Times New Roman', 60)
            text1 = f1.render("2 Player", False, (0, 0, 0))
            pos_text1 = (35, 390)

        elif flag2:
            f2 = pygame.font.SysFont('Times New Roman', 60)
            text2 = f2.render("3 Player", False, (0, 0, 0))
            pos_text2 = (260, 390)

        elif flag3:
            f3 = pygame.font.SysFont('Times New Roman', 60)
            text3 = f3.render("4 Player", False, (0, 0, 0))
            pos_text3 = (485, 390)

        elif flag4:
            f4 = pygame.font.SysFont('Times New Roman', 60)
            text4 = f4.render("2x2 Player", False, (0, 0, 0))
            pos_text4 = (710, 390)

        elif flag5:
            f5 = pygame.font.SysFont('Times New Roman', 90)
            text5 = f5.render("Quit", False, (0, 0, 0))
            pos_text5 = (395, 500)
        sec_screen.blit(text1, pos_text1)
        sec_screen.blit(text2, pos_text2)
        sec_screen.blit(text3, pos_text3)
        sec_screen.blit(text4, pos_text4)
        sec_screen.blit(text5, pos_text5)
        pygame.display.flip()
        clock.tick(FPS)


def start_screen():
    st_screen = pygame.display.set_mode((1000, 800))
    screen.blit(st_screen, (0, 0))
    play_button_pos = (250, 320, 750, 480)
    quit_button_pos = (350, 450, 650, 610)
    f1 = False
    f2 = False
    while True:
        st_screen.fill((225, 225, 225))
        f = pygame.font.SysFont('Times New Roman', 100)
        f_q = pygame.font.SysFont('Times New Roman', 100)
        text = f.render("Start Game", False, (0, 0, 0))
        text_q = f_q.render("Quit", False, (0, 0, 0))
        pos_text = (270, 345)
        pos_q = (390, 475)
        for event in pygame.event.get():
            if event.type == MOUSEMOTION and (
                    play_button_pos[0] <= event.pos[0] <= play_button_pos[2] and play_button_pos[1] <= event.pos[1] <=
                    play_button_pos[3]):
                f1 = True

            elif event.type == MOUSEMOTION and not (
                    play_button_pos[0] <= event.pos[0] <= play_button_pos[2] and play_button_pos[1] <= event.pos[1] <=
                    play_button_pos[3]):
                f1 = False

            if event.type == MOUSEMOTION and (
                    quit_button_pos[0] <= event.pos[0] <= quit_button_pos[2] and quit_button_pos[1] <= event.pos[1] <=
                    quit_button_pos[3]):
                f2 = True

            elif event.type == MOUSEMOTION and not (
                    quit_button_pos[0] <= event.pos[0] <= quit_button_pos[2] and quit_button_pos[1] <= event.pos[1] <=
                    quit_button_pos[3]):
                f2 = False

            if event.type == pygame.QUIT:
                terminate()
            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (play_button_pos[0] <= event.pos[0] <= play_button_pos[2] and
                   play_button_pos[1] <= event.pos[1] <= play_button_pos[3])):
                return True
            elif (event.type == pygame.MOUSEBUTTONDOWN and
                  (quit_button_pos[0] <= event.pos[0] <= quit_button_pos[2] and
                   quit_button_pos[1] <= event.pos[1] <= quit_button_pos[3])):
                terminate()
        if f1:
            f = pygame.font.SysFont('Times New Roman', 120)
            text = f.render("Start Game", False, (0, 0, 0))
            pos_text = (230, 335)
        elif f2:
            f_q = pygame.font.SysFont('Times New Roman', 120)
            text_q = f_q.render("Quit", False, (0, 0, 0))
            pos_q = (370, 465)
        st_screen.blit(text, pos_text)
        st_screen.blit(text_q, pos_q)
        pygame.display.flip()
        clock.tick(FPS)


running = True

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    screen.fill((225, 225, 225))
    clock = pygame.time.Clock()
    f1 = start_screen()
    if f1:
        mode_game = second_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((230, 230, 230))
        clock.tick(FPS)
        pygame.display.flip()

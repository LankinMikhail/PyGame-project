import pygame
import math
import os
from Collision.Bullet import Bullet, players, load_image, vertical_borders, horizontal_borders


class Player(pygame.sprite.Sprite):
    def __init__(self, team, x, y, angle, place):
        super().__init__()
        self.rect = None
        self.team = team
        self.x = x
        self.y = y
        self.angle = angle
        self.effect = None
        self.motion = "stop"
        self.rotation = "stop"
        self.is_alive = True
        self.width = 40
        self.height = 60
        if place == 1:
            self.w = 101
            self.s = 100
            self.a = 115
            self.d = 102
            self.q = 113
        elif place == 2:
            self.q = 121
            self.w = 105
            self.a = 106
            self.s = 107
            self.d = 108
        elif place == 3:
            self.q = 1073742052
            self.w = 1073741906
            self.a = 1073741904
            self.s = 1073741905
            self.d = 1073741903
        elif place == 4:
            self.q = 1073741922
            self.w = 1073741920
            self.a = 1073741916
            self.s = 1073741917
            self.d = 1073741918
        self.add(players)

    def render(self, screen):
        angle = round(self.angle)
        center = self.center()
        if self.team == 1:
            way = "танк1.png"
        elif self.team == 2:
            way = "танк2.png"
        elif self.team == 3:
            way = "танк3.png"
        elif self.team == 4:
            way = "танк4.png"
        texture = pygame.transform.rotate(pygame.transform.scale(load_image(os.path.dirname(__file__)[:-10]
                                                                            + "\\Assets\\" + way),
                                                                 (self.width, self.height)), angle + 180)
        self.rect = texture.get_rect()
        self.rect.x = round(self.x - center[0])
        self.rect.y = round(self.y - center[1])
        self.mask = pygame.mask.from_surface(texture)
        screen.blit(texture, (round(self.x - center[0]), round(self.y - center[1])))

    def update(self):
        base = (self.angle, self.x, self.y)
        angle = round(self.angle)
        if self.motion == "forward":
            self.y += math.cos(math.radians(angle))
            self.x += math.sin(math.radians(angle))
        elif self.motion == "back":
            self.y -= math.cos(math.radians(angle))
            self.x -= math.sin(math.radians(angle))
        if self.rotation == "left":
            self.angle -= 1.4
        elif self.rotation == "right":
            self.angle += 1.4
        self.angle %= 360
        for border in vertical_borders:
            if pygame.sprite.collide_mask(self, border):
                if self.motion != "stop":
                    self.x -= (self.x - base[1]) * 3
                    self.y -= (self.y - base[2]) * 3
                if self.rotation != "stop":
                    self.angle -= (self.angle - base[0]) * 3
                self.motion = "stop"
                self.rotation = "stop"
        for border in horizontal_borders:
            if pygame.sprite.collide_mask(self, border):
                if self.motion != "stop":
                    self.x -= (self.x - base[1]) * 3
                    self.y -= (self.y - base[2]) * 3
                if self.rotation != "stop":
                    self.angle -= (self.angle - base[0]) * 3
                self.motion = "stop"
                self.rotation = "stop"
        for player in players:
            if player != self and pygame.sprite.collide_mask(self, player):
                if self.motion != "stop":
                    self.x -= (self.x - base[1]) * 3
                    self.y -= (self.y - base[2]) * 3
                if self.rotation != "stop":
                    self.angle -= (self.angle - base[0]) * 3
                self.motion = "stop"
                self.rotation = "stop"

    def center(self):
        angle = round(self.angle)
        if self.angle <= 90:
            x = round((math.cos(math.radians(angle)) * self.width +
                       math.cos(math.radians(90 - angle)) * self.height) / 2)
            y = round((math.cos(math.radians(angle)) * self.height +
                       math.cos(math.radians(90 - angle)) * self.width) / 2)
        elif 90 < self.angle <= 180:
            x = round((math.cos(math.radians(angle - 90)) * self.height +
                       math.cos(math.radians(180 - angle)) * self.width) / 2)
            y = round((math.cos(math.radians(angle - 90)) * self.width +
                       math.cos(math.radians(180 - angle)) * self.height) / 2)
        elif 180 < self.angle <= 270:
            x = round((math.cos(math.radians(angle - 180)) * self.width +
                       math.cos(math.radians(270 - angle)) * self.height) / 2)
            y = round((math.cos(math.radians(angle - 180)) * self.height +
                       math.cos(math.radians(270 - angle)) * self.width) / 2)
        else:
            x = round((math.cos(math.radians(angle - 270)) * self.height +
                       math.cos(math.radians(360 - angle)) * self.width) / 2)
            y = round((math.cos(math.radians(angle - 270)) * self.width +
                       math.cos(math.radians(360 - angle)) * self.height) / 2)
        return x, y

    def front(self):
        angle = round(self.angle)
        return (round(self.x + (self.height * 0.6 * math.sin(math.radians(angle)))),
                round(self.y + (self.height * 0.6 * math.cos(math.radians(angle)))))

    def shoot(self, fps):
        velocity = 270 / fps
        angle = round(self.angle)
        front = self.front()
        return Bullet(3, front[0], front[1], velocity * math.sin(math.radians(angle)),
                      velocity * math.cos(math.radians(angle)), fps * 20)

    def death(self):
        self.is_alive = False
        self.rect.x = 10000
        self.rect.y = 10000

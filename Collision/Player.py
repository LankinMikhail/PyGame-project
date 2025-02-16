import pygame
import os
import math
from Collision.Bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self, team, x, y, angle):
        super().__init__()
        self.team = team
        self.x = x
        self.y = y
        self.angle = angle
        self.effect = None
        self.motion = "stop"
        self.rotating = "stop"
        self.is_alive = True
        self.width = 40
        self.height = 60
        if team == 1:
            self.w = "w"
            self.s = "s"
            self.a = "a"
            self.d = "d"
            self.q = "q"

    def render(self, screen):
        center = self.center()
        texture = pygame.transform.rotate(pygame.transform.scale(load_image(os.path.dirname(__file__)[:-10]
                                                                            + "\\Assets\\тест_модель.png"),
                                                                 (self.width, self.height)), self.angle + 180)
        screen.blit(texture, (round(self.x - center[0]), round(self.y - center[1])))

    def update(self):
        angle = round(self.angle)
        if self.motion == "forward":
            self.y += math.cos(math.radians(angle)) * 1.2
            self.x += math.sin(math.radians(angle)) * 1.2
        elif self.motion == "back":
            self.y -= math.cos(math.radians(angle)) * 1.2
            self.x -= math.sin(math.radians(angle)) * 1.2
        if self.rotating == "left":
            self.angle -= 1.5
        elif self.rotating == "right":
            self.angle += 1.5
        self.angle %= 360

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

    def shoot(self, fps):
        velocity = 270 / fps
        angle = round(self.angle)
        return Bullet(3, self.x, self.y, velocity * math.sin(math.radians(angle)),
                      velocity * math.cos(math.radians(angle)), fps * 20)


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        raise FileNotFoundError(name)
    image = pygame.image.load(fullname)
    return image

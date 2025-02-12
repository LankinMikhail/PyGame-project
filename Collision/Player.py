import pygame
import os
import sys
import math


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
        if team == 1:
            self.w = "w"
            self.s = "s"
            self.a = "a"
            self.d = "d"
            self.q = "q"

    def render(self, screen):
        texture = pygame.transform.rotate(pygame.transform.scale(load_image(os.path.dirname(__file__)[:-10]
                                                                            + "\\Assets\\тест_модель.png"),
                                                                 (50, 75)), self.angle + 180)
        screen.blit(texture, (round(self.x - 25 * 0), round(self.y - 37.5 * 0)))

    def update(self):
        if self.motion == "forward":
            self.y += math.cos(math.radians(self.angle))
            self.x += math.sin(math.radians(self.angle))
        elif self.motion == "back":
            self.y -= math.cos(math.radians(self.angle))
            self.x -= math.sin(math.radians(self.angle))
        if self.rotating == "left":
            self.angle -= 1
        elif self.rotating == "right":
            self.angle += 1


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        raise FileNotFoundError(name)
    image = pygame.image.load(fullname)
    return image

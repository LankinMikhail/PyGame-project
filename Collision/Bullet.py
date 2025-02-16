import pygame
import os
from pygame import gfxdraw
from Collision.Border import vertical_borders, horizontal_borders


class Bullet(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, vx, vy, life):
        super().__init__()
        self.rect = pygame.Rect(x - radius, y - radius, 2 * radius, 2 * radius)
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = life
        texture = load_image(os.path.dirname(__file__)[:-10] + "\\Assets\\пуля.png")
        self.mask = pygame.mask.from_surface(texture)

    def update(self):
        self.life -= 1
        if self.life == 0:
            self.delete()
            return
        self.x += self.vx
        self.y += self.vy
        self.rect = pygame.Rect(round(self.x - self.radius), round(self.y - self.radius), 2 * self.radius, 2 * self.radius)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
        for player in players:
            if pygame.sprite.collide_mask(self, player):
                player.death()
                self.delete()
                return

    def render(self, screen):
        gfxdraw.aacircle(screen, round(self.x), round(self.y), self.radius, (0, 0, 0))
        gfxdraw.filled_circle(screen, round(self.x), round(self.y), self.radius, (0, 0, 0))

    def delete(self):
        bullets.remove(self)


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        raise FileNotFoundError(name)
    image = pygame.image.load(fullname)
    return image


bullets = []
players = pygame.sprite.Group()

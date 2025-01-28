import pygame
from pygame import gfxdraw
from Collision.Border import vertical_borders, horizontal_borders


class Bullet(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, vx, vy, life):
        super().__init__()
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.radius = radius
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = life

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        if self.life == 0:
            bullets.remove(self)
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        elif pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx

    def render(self, screen):
        gfxdraw.aacircle(screen, self.x, self.y, self.radius, (0, 0, 0))
        gfxdraw.filled_circle(screen, self.x, self.y, self.radius, (0, 0, 0))


bullets = []

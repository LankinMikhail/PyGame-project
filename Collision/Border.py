import pygame


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if x1 == x2:
            self.add(vertical_borders)
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
            self.mask = pygame.mask.from_surface(pygame.Surface((1, y2 - y1)))
        else:
            self.add(horizontal_borders)
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
            self.mask = pygame.mask.from_surface(pygame.Surface((x2 - x1, 1)))

    def render(self, screen):
        if self.x1 == self.x2:
            pygame.draw.rect(screen, "green", self.rect)
        else:
            pygame.draw.rect(screen, "red", self.rect)


horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

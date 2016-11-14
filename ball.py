import pygame
import random

class Ball(pygame.sprite.Sprite):

    def __init__(self, screen, color,):
        super().__init__()
        self.image = pygame.Surface((7,7))
        self.image.fill(color)
        self.screen = screen
        self.vx = random.randint(3, 7)
        self.vy = random.randint(3, 7)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.left += self.vx
        self.rect.top += self.vy
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.vx = -self.vx
        if self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
            self.vy = -self.vy

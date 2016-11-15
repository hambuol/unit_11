import pygame
import random

class Ball(pygame.sprite.Sprite):

    def __init__(self, screen, color,):
        super().__init__()
        self.image = pygame.Surface((7,7))
        self.image.fill(color)
        self.screen = screen
        self.speedx = 6
        self.speedy = 4
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.left += self.speedx
        self.rect.top += self.speedy
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speedx = -self.speedx
        if self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
            self.speedy = -self.speedy

    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.speedy = -self.speedy
            self.speedx = -self.speedx

    def collide2(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speedy = -self.speedy
            self.speedx = -self.speedx


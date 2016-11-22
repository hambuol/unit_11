# imports needed moduel, pygame
import pygame


class Paddle(pygame.sprite.Sprite):
    """class sets what is needed for the paddle"""

    def __init__(self, color):
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()

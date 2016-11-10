import pygame

class Brick(pygame.sprite.Sprite):


    def __init__(self, width, color):
        super().__init__()
        self.BRICK_HEIGHT = 8
        self.width = width
        self.image = pygame.Surface((self.width, self.BRICK_HEIGHT))
        self.rect = self.image.get_rect()
        self.image.fill(color)
        pygame.init()

    def update(self):
        pass


    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            pass




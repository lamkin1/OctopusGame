import pygame

class Background:
    def __init__(self, screen, name):
        self.image = pygame.image.load(name).convert()
        self.image = pygame.transform.scale(self.image, (screen.get_width(), screen.get_height()))
        self.rect = self.image.get_rect(center=screen.get_rect().center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
import pygame
class Portal:
    def __init__(self, screen):
        self.image = pygame.image.load("portal.png").convert_alpha()
        self.rect = self.image.get_rect(center=(700, 700))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    # def getx(self):
    #     return self.x
    #
    # def gety(self):
    #     return self.y
    #
    # def setx(self, inputx):
    #     self.x = inputx
    #
    # def sety(self, inputy):
    #     self.y = inputy

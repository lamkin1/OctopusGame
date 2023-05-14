import pygame
import math

class Ink(pygame.sprite.Sprite):
    def __init__(self, position, angle):
        pygame.sprite.Sprite.__init__(self)
        ink_image = pygame.image.load('ink.png').convert_alpha()
        self.image = pygame.transform.rotate(ink_image, angle)
        self.rect = self.image.get_rect(center=position)
        self.velocity = 1.5
        self.angle = angle
        self.dx = math.sin(angle * math.pi / 180) * self.velocity
        self.dy = math.cos(angle * math.pi / 180) * -self.velocity
        self.opacity = 255

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.opacity -= 3  # decrease opacity by 3 every frame
        self.image.set_alpha(self.opacity)  # set new alpha value for image
        if self.opacity <= 0:
            self.kill()  # remove sprite from g

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def getangle(self):
        return self.angle
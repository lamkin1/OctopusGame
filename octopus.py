import pygame
import math

class Octopus(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.image.load("octopus.png").convert_alpha()
        # load octopus image and get its rect
        self.image = pygame.image.load('octopus.png').convert_alpha()
        self.image = self.image_orig.copy()
        image_size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.angle = 0
        self.maxMoveSpeed = 5
        self.moveSpeed = 5

        # set octopus position to center of screen
        self.rect.center = screen.get_rect().center

    def reset(self, screen):
        self.movex = 0
        self.movey = 0
        self.rect.center = screen.get_rect().center

    def draw(self, screen):
        # draw octopus on screen
        self.image = pygame.transform.rotate(self.image_orig, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)

    def control(self, mouse_pos):
        dx, dy = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery
        self.angle = 90 + math.degrees(math.atan2(dy, dx))
        # print(self.angle)

        length = math.sqrt(dx * dx + dy * dy)
        print(length)
        self.moveSpeed = self.maxMoveSpeed if length > 200 else (length / 200) * self.maxMoveSpeed

        movement_x = math.sin(self.angle * (0.0174533)) * self.moveSpeed
        movement_y = math.cos(self.angle * (0.0174533)) * self.moveSpeed * (-1)

        self.movey += movement_y
        self.movex += movement_x
        # print(f'movex: {self.movex} movey: {self.movey}')
        self.update(mouse_pos)

    def update(self, mouse_pos):
        dx, dy = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery

        self.angle = 90 + math.degrees(math.atan2(dy, dx))

        deceleration = .995
        self.movex *= deceleration if abs(self.movex) > .7 else 1
        self.movey *= deceleration if abs(self.movey) > .7 else 1

        #print(self.movex)

        self.rect.centerx += self.movex
        #print(self.rect.centerx)
        self.rect.centery += self.movey


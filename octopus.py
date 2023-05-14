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
        self.maxMoveSpeed = 2
        self.moveSpeed = 2

        # set octopus position to center of screen
        self.rect.center = screen.get_rect().center

    def getPosition(self):
        return self.rect

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

        movement_x = math.sin(self.angle * 0.0174533) * self.moveSpeed
        movement_y = math.cos(self.angle * 0.0174533) * self.moveSpeed * (-1)

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

        self.rect.centerx += self.movex
        self.rect.centery += self.movey

        # Screen dimensions
        screen_width = 1920
        screen_height = 1080

        # If the octopus crosses the screen boundaries, make it appear on the opposite side
        if self.rect.right < 0:
            self.rect.left = screen_width
        elif self.rect.left > screen_width:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = screen_height
        elif self.rect.top > screen_height:
            self.rect.bottom = 0



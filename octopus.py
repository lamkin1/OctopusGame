import pygame
import math

from energycell import EnergyCell
from ink import Ink


class Octopus(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.ink_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
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
        self.maxMoveSpeed = 1.2
        self.moveSpeed = 1.2
        self.ink_cooldown = 0
        # set octopus position to center of screen
        self.rect.center = screen.get_rect().center
        self.rect.centery = screen.get_rect().height - 350  # move the octopus 100 pixels from the bottom of the screen
        self.hasCell = False

    def getPosition(self):
        return self.rect

    def reset(self, screen):
        self.movex = 0
        self.movey = 0
        self.rect.center = screen.get_rect().center
        self.rect.centery = screen.get_rect().height - 350  # move the octopus 100 pixels from the bottom of the screen


    def draw(self, screen):
        # draw octopus on screen
        self.image = pygame.transform.rotate(self.image_orig, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)

        for ink in self.all_sprites:
            ink.draw(screen)

    def control(self, mouse_pos):
        dx, dy = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery
        self.angle = 90 + math.degrees(math.atan2(dy, dx))
        # print(self.angle)

        length = math.sqrt(dx * dx + dy * dy)
        print(length)
        self.moveSpeed = self.maxMoveSpeed if length > 200 else (length / 200) * self.maxMoveSpeed

        movement_x = math.sin(self.angle * 0.0174533) * self.moveSpeed
        movement_y = math.cos(self.angle * 0.0174533) * self.moveSpeed * (-1)

        self.movey += movement_y if abs(self.movey) < 1 else 0
        self.movex += movement_x if abs(self.movex) < 1 else 0
        # print(f'movex: {self.movex} movey: {self.movey}')
        self.update(mouse_pos)

    def update(self, mouse_pos):
        dx, dy = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery

        self.angle = 90 + math.degrees(math.atan2(dy, dx))

        deceleration = .90
        self.movex *= deceleration if abs(self.movex) > .6 else 1
        self.movey *= deceleration if abs(self.movey) > .6 else 1
        print(self.movex)

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


        self.rect.centerx += self.movex
        # print(self.rect.centerx)
        self.rect.centery += self.movey

        for ink in self.all_sprites:
            ink.update()




    def shoot_ink(self):

        # Create 5 ink particles at slightly different positions
        ink_sprites = pygame.sprite.Group()
        for i in range(10):
            x_offset = math.cos(math.radians(i * 72)) * 20
            y_offset = math.sin(math.radians(i * 72)) * 20
            position = (self.rect.centerx + x_offset, self.rect.centery + y_offset)
            angle = 180 + self.angle + (i - 2) * 10
            ink = Ink(position, angle)
            ink_sprites.add(ink)


        # Add ink particles to the global sprite group
        self.all_sprites.add(ink_sprites)
        # set ink cooldown
        self.ink_cooldown = 30

    def sethascell(self):
        self.hasCell = True


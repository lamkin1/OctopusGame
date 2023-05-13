import pygame
import math

animation = 4
moveSpeed = 5

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

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
        self.pos = [screen_width // 2, screen_height // 2]

        # set octopus position to center of screen
        self.rect.center = screen.get_rect().center

    def draw(self, screen):
        # draw octopus on screen
        self.image = pygame.transform.rotate(self.image_orig, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)

    def control(self, mouse_pos):
        dx, dy = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery
        self.angle = 90 + math.degrees(math.atan2(dy, dx))
        print(self.angle)
        movement_x = math.sin(self.angle * (0.0174533)) * moveSpeed
        movement_y = math.cos(self.angle * (0.0174533)) * moveSpeed * (-1)
        self.movey += movement_y
        self.movex += movement_x
        print(f'movex: {self.movex} movey: {self.movey}')
        self.update(mouse_pos)


    def update(self, mouse_pos):
        dx, dy = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery
        self.angle = 90 + math.degrees(math.atan2(dy, dx))
        self.rect.centerx += self.movex
        self.rect.centery += self.movey

class Background:
    def __init__(self, screen):
        self.image = pygame.image.load("starterBackground.png").convert()
        self.image = pygame.transform.scale(self.image, (screen.get_width(), screen.get_height()))
        self.rect = self.image.get_rect(center=screen.get_rect().center)

    def draw(self, screen):

        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    pygame.display.set_caption('My Game')

    background = Background(screen)
    octopus = Octopus(screen)

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT or event.key == ord(' '):
                    octopus.control(mouse_pos)
                    print('Move')

        #draw the background and octopus on the screen

        octopus.update(mouse_pos)
        screen.fill((0, 0, 0))
        background.draw(screen)
        octopus.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
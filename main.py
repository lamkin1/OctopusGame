import pygame
import math

pygame.init()

# Set up the screen
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

class Background:
    def __init__(self, screen):
        self.image = pygame.image.load("starterBackground.png").convert()
        self.image = pygame.transform.scale(self.image, (screen.get_width(), screen.get_height()))
        self.rect = self.image.get_rect(center=screen.get_rect().center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Octopus:
    def __init__(self, screen):
        self.image_orig = pygame.image.load("octopus.png").convert_alpha()
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect(center=screen.get_rect().center)
        self.angle = 0

    def draw(self, screen):
        self.image = pygame.transform.rotate(self.image_orig, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)

    def update(self, mouse_pos):
        dx, dy = mouse_pos[0] - self.rect.centerx, mouse_pos[1] - self.rect.centery
        self.angle = 90 + math.degrees(math.atan2(dy, dx))

background = Background(screen)
octopus = Octopus(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    mouse_pos = pygame.mouse.get_pos()
    octopus.update(mouse_pos)
    screen.fill((0, 0, 0))
    background.draw(screen)
    octopus.draw(screen)
    pygame.display.flip()

pygame.quit()

if __name__ == '__main__':
    main()

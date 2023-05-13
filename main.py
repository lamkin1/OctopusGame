import pygame

class Octopus:
    def __init__(self, screen):
        # load octopus image and get its rect
        self.image = pygame.image.load('octopus.png').convert_alpha()
        image_size = self.image.get_size()
        self.rect = self.image.get_rect()

        # set octopus position to center of screen
        self.rect.center = screen.get_rect().center

    def draw(self, screen):
        # draw octopus on screen
        screen.blit(self.image, self.rect)


class Background:
    def __init__(self, screen):
        self.image = pygame.image.load("starterBackground.png").convert()
        self.image = pygame.transform.scale(self.image, (screen.get_width(), screen.get_height()))
        self.rect = self.image.get_rect()

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #draw the background and octopus on the screen
        background.draw(screen)
        octopus.draw(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

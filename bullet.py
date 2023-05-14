import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, speed, player_rect, color):
        super().__init__()
        # initialized with a starting position, direction, and speed
        self.color = color  # store the color for later reference
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)  # we're creating a bigger Surface to accommodate the circle
        pygame.draw.circle(self.image, self.color, (5, 5), 5)
        self.rect = self.image.get_rect(center=position)
        self.direction = direction
        self.speed = speed
        self.player_rect = player_rect



    # moves the bullet in its direction at the given speed, checks if the bullet has gone off the screen
    def update(self):
        self.rect.move_ip(self.direction * self.speed)
        print(self.rect.center)
        # Check if the bullet is off the screen
        if not pygame.display.get_surface().get_rect().colliderect(self.rect):
            print('hit')
            self.kill()

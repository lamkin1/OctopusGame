import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, direction, speed, player_rect):
        super().__init__()
        # initialized with a starting position, direction, and speed
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
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

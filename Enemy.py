import pygame
import random

screen_width = 1920
screen_height = 1080

class Enemy(pygame.sprite.Sprite):
    def __init__(self, player_position):
        super().__init__()
        self.image_orig = pygame.image.load("otter.png").convert_alpha()
        # load octopus image and get its rect
        self.image = pygame.image.load('otter.png').convert_alpha()
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.generate_random_position(player_position)
        self.angle = 45

    def draw(self, screen):
        # draw octopus on screen
        self.image = pygame.transform.rotate(self.image_orig, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)

    def generate_random_position(self, player_position):
        while True:
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            if self.is_far_from_player(player_position, (x, y)):
                return x, y

    def is_far_from_player(self, player_position, enemy_position):
        min_distance = 100  # Minimum distance between player and enemy
        return pygame.math.Vector2(enemy_position).distance_to(player_position) >= min_distance


    def spawn_enemies(self, numEnemies, playerPosition):
        enemies = pygame.sprite.Group()
        for i in range(numEnemies):
            enemy = Enemy(playerPosition)
            enemies.add(enemy)
        return enemies

    def update(self, bullets):
        collisions = pygame.sprite.spritecollide(self, bullets, True)
        if collisions:
            self.kill()
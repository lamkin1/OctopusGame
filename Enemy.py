import pygame
import random
import math

screen_width = 1920
screen_height = 1080
def blend_colors(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    # Blend the colors
    r = min(r1, r2)
    g = min(g1, g2)
    b = min(b1, b2)

    return (r, g, b)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, player_position):
        super().__init__()
        self.image_orig = pygame.image.load("otter.png").convert_alpha()
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        current_size = self.rect.size
        new_size = (current_size[0] // 2, current_size[1] // 2)
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.rect.center = self.generate_random_position(player_position)
        self.angle = 45
        self.speed = 1
        self.hit_colors = set()  # Add this line
        self.color = (255, 255, 255)  # Add this line


    def update(self, player_pos, bullets, scoreboard):
        dx = player_pos[0] - self.rect.centerx
        dy = player_pos[1] - self.rect.centery
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Define the colors of the bullets
        bullet_colors = {(255, 0, 0), (0, 255, 0), (0, 0, 255)}  # for example

        collisions = pygame.sprite.spritecollide(self, bullets, True)

        for bullet in collisions:
            # Get the color of the bullet
            bullet_color = bullet.color

            # Add the bullet color to the hit colors
            self.hit_colors.add(bullet_color)

            # Blend the bullet color with the current color of the enemy
            blended_color = blend_colors(bullet_color, self.color)

            # Create a new surface with the blended color
            stain = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            stain.fill(blended_color)  # Apply the blended color with half transparency

            # Blend the stain with the enemy image
            self.image.blit(stain, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            self.image_orig = self.image.copy()

        if distance > 0:
            dx_normalized = dx / distance
            dy_normalized = dy / distance
            self.rect.x += dx_normalized * self.speed
            self.rect.y += dy_normalized * self.speed

        # If the enemy has been hit by all colors
        if len(self.hit_colors) >= len(bullet_colors):
            self.kill()
            scoreboard.increment_score()

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
        min_distance = 500  # Minimum distance between player and enemy
        return pygame.math.Vector2(enemy_position).distance_to(player_position) >= min_distance


    def spawn_enemies(self, numEnemies, playerPosition):
        enemies = pygame.sprite.Group()
        for i in range(numEnemies):
            enemy = Enemy(playerPosition)
            enemies.add(enemy)
        return enemies

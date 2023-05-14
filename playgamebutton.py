import pygame

class PlayGameButton:
    def __init__(self, screen):
        self.image = pygame.image.load('gameButton.png')
        scale_factor = 0.08  # Scale the image to be 10% of its original size
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale_factor), int(self.image.get_height() * scale_factor)))
        self.rect = self.image.get_rect(center=(screen.get_width() // 2, (screen.get_height() // 2) + 125))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

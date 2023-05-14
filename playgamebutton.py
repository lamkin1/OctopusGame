import pygame

class PlayGameButton:
    def __init__(self, screen):
        self.image_orig = pygame.image.load("gameButton.png").convert_alpha()
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        current_size = self.rect.size
        new_size = (current_size[0] // 20, current_size[1] // 20)
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect.inflate_ip(50, 25)  # Increase the button size by 150 pixels horizontally and 50 pixels vertically

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)
        screen.blit(self.image, self.rect)

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


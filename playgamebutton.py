import pygame

class PlayGameButton:
    def __init__(self, screen):
        self.font = pygame.font.SysFont(None, 30)
        self.text = self.font.render("Play Game", True, (255, 255, 255))
        self.rect = self.text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        self.rect.inflate_ip(50, 25)  # Increase the button size by 150 pixels horizontally and 50 pixels vertically

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect, 2)
        screen.blit(self.text, self.rect)

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
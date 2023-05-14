import pygame

class EnergyCell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Load image
        self.image = pygame.image.load("energycell.png").convert_alpha()

        # Set rect
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def update(self, octopus, energy_cells):
        for cell in energy_cells:
            if pygame.sprite.collide_rect(cell, octopus):
                # Remove the energy cell from all sprite groups and kill the sprite
                self.kill()
                octopus.flipSkin()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
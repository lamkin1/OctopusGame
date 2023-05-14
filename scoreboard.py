import pygame
pygame.font.init()


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)  # choose the font and size

    def increment_score(self):
        self.score += 1

    def draw(self, screen):
        score_text = "Score: " + str(self.score)
        text = self.font.render(score_text, True, (255, 255, 255))  # the color is white
        screen.blit(text, (10, 10))  # you can position it where you want

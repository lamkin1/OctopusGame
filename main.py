import pygame
import gamestate
import octopus

animation = 4

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

def main():
    pygame.init()

    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    player = octopus.Octopus(screen)
    level_manager = gamestate.GameState(player)
    pygame.display.set_caption('My Game')



    while True:
        level_manager.state_manager(screen)

if __name__ == '__main__':
    main()

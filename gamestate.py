import pygame
import background
import bullet
import playgamebutton
import portal
from bullet import Bullet



class GameState:
    def __init__(self):
        self.state = 'intro'
        self.color_iter = iter([(255, 0, 0), (0, 255, 0), (0, 0, 255)])  # Red, Green, Blue
        self.level_backgrounds = ["raccoon.png", "starterBackground.png"]
        self.bullet_group = pygame.sprite.Group()


    def intro(self, screen, octopus):
        mouse_pos = pygame.mouse.get_pos()
        level_background = background.Background(screen, "raccoon.png")
        play_game_button = playgamebutton.PlayGameButton(screen)
        bullet_group = pygame.sprite.Group()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    if event.key == pygame.K_LEFT or event.key == ord(' '):
                        octopus.control(mouse_pos)
                        # print('Move')
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_game_button.clicked(pygame.mouse.get_pos()):
                        octopus.reset(screen)
                        self.state = 'main_game'
                        self.main_game(screen, octopus)
                        print("Starting the game...")

                    # Get the direction vector between the mouse position and the player position
                    dx, dy = event.pos[0] - octopus.rect.centerx, event.pos[1] - octopus.rect.centery
                    direction = pygame.Vector2(dx, dy).normalize()

                    # Create a new bullet and add it to the group
                    # Cycle to the next color
                    color = next(self.color_iter, None)
                    if color is None:  # If we've reached the end of the list, reset the iterator
                        self.color_iter = iter([(255, 0, 0), (0, 255, 0), (0, 0, 255)])  # Red, Green, Blue
                        color = next(self.color_iter)

                    shots = Bullet(octopus.rect.center, direction, 10, octopus.rect, color)
                    #print(
                    #    f"Bullet position: {shots.rect.center}, direction: {shots.direction}, speed: {shots.speed}")

                    bullet_group.add(shots)


            # draw the background and octopus and portal on the screen
            mouse_pos = pygame.mouse.get_pos()
            octopus.update(mouse_pos)
            screen.fill((0, 0, 0))
            level_background.draw(screen)
            octopus.draw(screen)
            play_game_button.draw(screen)
            bullet_group.update()
            for bullet in bullet_group.sprites():
                print(f"Bullet position: {bullet.rect.center}, direction: {bullet.direction}, speed: {bullet.speed}")

            bullet_group.draw(screen)
            pygame.display.flip()

    def main_game(self, screen, octopus):
        level_background = background.Background(screen, "starterBackground.png")
        first_portal = portal.Portal(screen)
        bullet_group = pygame.sprite.Group()

        # Define colors and iterator


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    if event.key == pygame.K_LEFT or event.key == ord(' '):
                        octopus.control(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the direction vector between the mouse position and the player position
                    dx, dy = event.pos[0] - octopus.rect.centerx, event.pos[1] - octopus.rect.centery
                    direction = pygame.Vector2(dx, dy).normalize()

                    # Cycle to the next color
                    # Cycle to the next color
                    color = next(self.color_iter, None)
                    if color is None:  # If we've reached the end of the list, reset the iterator
                        self.color_iter = iter([(255, 0, 0), (0, 255, 0), (0, 0, 255)])  # Red, Green, Blue
                        color = next(self.color_iter)

                    # Create a new bullet with the current color and add it to the group
                    bullet = Bullet(octopus.rect.center, direction, 10, octopus.rect, color)
                    bullet_group.add(bullet)

            # update the game state
            mouse_pos = pygame.mouse.get_pos()
            octopus.update(mouse_pos)
            bullet_group.update()

            # draw the game objects on the screen
            screen.fill((0, 0, 0))
            level_background.draw(screen)
            octopus.draw(screen)
            bullet_group.draw(screen)
            first_portal.draw(screen)
            pygame.display.flip()

    # def main_game(self, screen, octopus):
    #     mouse_pos = pygame.mouse.get_pos()
    #     level_background = background.Background(screen, "starterBackground.png")
    #     first_portal = portal.Portal(screen)
    #     bullet_group = pygame.sprite.Group()
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #         elif event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 pygame.quit()
    #             if event.key == pygame.K_LEFT or event.key == ord(' '):
    #                 octopus.control(mouse_pos)
    #                 # print('Move')
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             # Get the direction vector between the mouse position and the player position
    #             dx, dy = event.pos[0] - octopus.rect.centerx, event.pos[1] - octopus.rect.centery
    #             direction = pygame.Vector2(dx, dy).normalize()
    #             # Create a new bullet and add it to the group
    #             shots = bullet.Bullet(octopus.rect.center, direction, 10, octopus.rect)
    #             bullet_group.add(shots)
    #
    #     # draw the background and octopus and portal on the screen
    #     mouse_pos = pygame.mouse.get_pos()
    #     octopus.update(mouse_pos)
    #     screen.fill((0, 0, 0))
    #     level_background.draw(screen)
    #     octopus.draw(screen)
    #     bullet_group.update()
    #     bullet_group.draw(screen)
    #     first_portal.draw(screen)
    #     pygame.display.flip()

    def state_manager(self, screen, octopus):
        if self.state == 'intro':
            self.intro(screen, octopus)
        if self.state == 'main_game':
            self.main_game(screen, octopus)


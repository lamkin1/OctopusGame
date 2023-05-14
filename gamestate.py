import pygame
import background
import bullet
import playgamebutton
import Enemy
import portal
import scoreboard
from octopus import Octopus
from bullet import Bullet

from energycell import EnergyCell

scoreboard = scoreboard.ScoreBoard()

class GameState:
    def __init__(self, octopus):
        self.color_iter = iter([(255, 0, 0), (0, 255, 0), (0, 0, 255)])  # Red, Green, Blue
        self.state = 'intro'
        self.octopus = octopus
        self.bullet_group = pygame.sprite.Group()

    def intro(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        level_background = background.Background(screen, "titleBackground.jpeg")
        play_game_button = playgamebutton.PlayGameButton(screen)
        bullet_group = pygame.sprite.Group()
        check = True
        while check:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    if event.key == pygame.K_LEFT or event.key == ord(' '):
                        self.octopus.control(mouse_pos)
                        self.octopus.shoot_ink()
                        # print('Move')
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_game_button.clicked(pygame.mouse.get_pos()):
                        self.octopus.reset(screen)
                        self.state = 'main_game'
                        self.main_game(screen)
                        check = False
                        break
                        print("Starting the game...")

                    # Get the direction vector between the mouse position and the player position
                    dx, dy = event.pos[0] - self.octopus.rect.centerx, event.pos[1] - self.octopus.rect.centery
                    direction = pygame.Vector2(dx, dy).normalize()

                    color = next(self.color_iter, None)
                    if color is None:  # If we've reached the end of the list, reset the iterator
                        self.color_iter = iter([(255, 0, 0), (0, 255, 0), (0, 0, 255)])  # Red, Green, Blue
                        color = next(self.color_iter)
                    # Create a new bullet and add it to the group
                    shots = Bullet(self.octopus.rect.center, direction, 10, self.octopus.rect, color)
                    # print(
                    # Cycle to the next color
                    color = next(self.color_iter, None)
                    if color is None:  # If we've reached the end of the list, reset the iterator
                        self.color_iter = iter([(255, 0, 0), (0, 255, 0), (0, 0, 255)])  # Red, Green, Blue
                        color = next(self.color_iter)

                    shots = Bullet(self.octopus.rect.center, direction, 10, self.octopus.rect, color)
                    #print(
                    #    f"Bullet position: {shots.rect.center}, direction: {shots.direction}, speed: {shots.speed}")

                    bullet_group.add(shots)

            if not check:
                break
            # draw the background and octopus and portal on the screen
            mouse_pos = pygame.mouse.get_pos()
            self.octopus.update(mouse_pos)
            screen.fill((0, 0, 0))
            level_background.draw(screen)
            self.octopus.draw(screen)
            play_game_button.draw(screen)
            bullet_group.update()
            for bullet in bullet_group.sprites():
                print(f"Bullet position: {bullet.rect.center}, direction: {bullet.direction}, speed: {bullet.speed}")

            bullet_group.draw(screen)
            pygame.display.flip()

    def main_game(self, screen):
        level_background = background.Background(screen, "starterBackground.png")
        first_portal = portal.Portal(screen)
        bullet_group = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.enemy_spawn_delay = 10000
        self.spawn_timer = 0
        self.spawn_rate = 2
        enemies = pygame.sprite.Group()
        enemy = Enemy.Enemy(self.octopus.rect.center)
        enemy_group = enemy.spawn_enemies(10, self.octopus.rect.center)
        for enemy in enemy_group:
            enemies.add(enemy)
        # Create sprite group
        energy_cells = pygame.sprite.Group()
        # Create EnergyCell instance
        cell = EnergyCell(500, 500)
        # Add EnergyCell instance to sprite group
        energy_cells.add(cell)

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
                        self.octopus.control(pygame.mouse.get_pos())
                        self.octopus.shoot_ink()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the direction vector between the mouse position and the player position
                    dx, dy = event.pos[0] - self.octopus.rect.centerx, event.pos[1] - self.octopus.rect.centery
                    direction = pygame.Vector2(dx, dy).normalize()
                    # Create a new bullet and add it to the group
                    color = next(self.color_iter, None)
                    if color is None:  # If we've reached the end of the list, reset the iterator
                        self.color_iter = iter([(255, 0, 0), (0, 255, 0), (0, 0, 255)])  # Red, Green, Blue
                        color = next(self.color_iter)
                    shots = Bullet(self.octopus.rect.center, direction, 10, self.octopus.rect, color)
                    bullet_group.add(shots)
                    for bullet in bullet_group.sprites():
                        print(
                            f"Bullet position: {bullet.rect.center}, direction: {bullet.direction}, speed: {bullet.speed}")

            # update the game state
            mouse_pos = pygame.mouse.get_pos()
            bullet_group.update()
            self.spawn_timer += 10
            if self.enemy_spawn_delay - self.spawn_timer < 1000:
                enemy_group = enemy.spawn_enemies(self.spawn_rate, self.octopus.rect.center)
                for enemy in enemy_group:
                    enemies.add(enemy)
                self.spawn_timer = 0
                self.spawn_rate += 1

            enemies.update(self.octopus.rect.center, bullet_group, scoreboard)

            self.octopus.update(mouse_pos)
            self.octopus.update(mouse_pos)

            for bullet in bullet_group.sprites():
                print(f"Bullet position: {bullet.rect.center}, direction: {bullet.direction}, speed: {bullet.speed}")

            # draw the game objects on the screen
            screen.fill((0, 0, 0))
            level_background.draw(screen)
            self.octopus.draw(screen)
            bullet_group.draw(screen)
            enemies.draw(screen)
            scoreboard.draw(screen)
            scoreboard.increment_score(0)
            energy_cells.update(self.octopus, energy_cells)
            energy_cells.draw(screen)
            deathcollisions = pygame.sprite.spritecollide(self.octopus, enemies, True)
            collisions = pygame.sprite.spritecollide(self.octopus, energy_cells, True)
            if deathcollisions:
                break
            if collisions:
                print("COLLIDING COLLIDING")
                self.octopus.sethascell()
                self.octopus.flipSkin()

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

    def state_manager(self, screen):
        if self.state == 'intro':
            self.intro(screen)
        if self.state == 'main_game':
            self.main_game(screen)

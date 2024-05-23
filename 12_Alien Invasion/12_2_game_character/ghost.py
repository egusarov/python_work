import pygame


class Ghost:
    """A class to manage the ghost."""

    def __init__(self, gw_game):
        """Initialize the ghost and set its starting position."""
        self.screen = gw_game.screen
        self.screen_rect = gw_game.screen.get_rect()

        # Load the ghost image and get its rect
        self.image = pygame.image.load('python_work/12_Alien Invasion/12_2_game_character/images/ghost.bmp')
        self.rect = self.image.get_rect()

        # Start each new ghost at the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ghost at its current location."""
        self.screen.blit(self.image, self.rect)

    
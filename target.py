import pygame

class Target:
    """A class to manage the target."""

    def __init__(self, sdm_game):
        """Initialize the ship and set its starting position."""

        self.screen = sdm_game.screen
        self.screen_rect = sdm_game.screen.get_rect()

        # Load the target image and get its rect.
        self.image = pygame.image.load('images/target.png')
        self.rect = self.image.get_rect()

        # Start each new target at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the target at its current location."""
        self.screen.blit(self.image, self.rect)
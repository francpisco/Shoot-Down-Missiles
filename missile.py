import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
    """A class to manage oncoming missiles to be shoot down."""

    def __init__(self, sdm_game):
        """
        Create a missile object at a random location at the top of
        the screen.
        """

        super().__init__()
        self.screen = sdm_game.screen
        self.settings = sdm_game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/missile_2.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midtop

        # Store decimal values of the missile position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        """Move the missile down the screen."""
        # Update the decimal position of the missile.
        self.y += self.settings.missile_speed

        # Update the rect position.
        self.rect.y = self.y

    def blitme(self):
        """Draw missile on current location."""
        self.screen.blit(self.image, self.rect)

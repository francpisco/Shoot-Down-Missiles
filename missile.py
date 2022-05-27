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
        self.color = self.settings.missile_color

        # Create a missile a origin and then place it at midscreen top
        self.rect = pygame.Rect(0, 0, self.settings.missile_width,
                                self.settings.missile_height)
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

    def draw_missile(self):
        """Draw missile on current location."""
        pygame.draw.rect(self.screen, self.color, self.rect)

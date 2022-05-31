import pygame
from pygame.sprite import Sprite
from random import randint, uniform
from math import cos, sin

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
        
        self._set_initial_position()
        self._set_initial_direction()
        self._set_initial_curve()

        # Store decimal values of the missile position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        """Move the missile down the screen."""
        # Update the decimal position of the missile.
        self.y += self.settings.missile_speed * cos(self.angle)
        self.x += self.settings.missile_speed * sin(self.angle)

        # Update the rect position.
        self.rect.y = self.y
        self.rect.x = self.x

        self._update_angle()
        self._update_curve()

    def draw_missile(self):
        """Draw missile on current location."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def _set_initial_position(self):
        """
        Calculate an initial random position for the missile at the top of 
        the screen.
        """
        pos_x = randint(0, self.screen_rect.width)
        self.rect.midbottom = (pos_x, 0)

    def _set_initial_direction(self):
        """
        Calculate an initial direction for the missile.
        It can vary between negative maximum and positive max angle.
        """
        self.angle = uniform(-self.settings.missile_max_angle,
                             self.settings.missile_max_angle)

    def _set_initial_curve(self):
        """
        Calculate an initial curvature to missile course.
        """
        self.curve = uniform(-self.settings.missile_max_curve,
                             self.settings.missile_max_curve)

    def _update_angle(self):
        """
        Update angle of missile tragectory as a function of curvature.
        """
        self.angle += self.curve


    def _update_curve(self):
        """
        Update curve of missile tragectory gradually.
        """
        curve_increment = uniform(-self.settings.missile_max_curve * 0.1,
                                  self.settings.missile_max_curve * 0.1)
        if (self.curve + curve_increment) > self.settings.missile_max_curve:
            self.curve -= curve_increment
        elif (self.curve + curve_increment) < -self.settings.missile_max_curve:
            self.curve -= curve_increment
        else:
            self.curve += curve_increment


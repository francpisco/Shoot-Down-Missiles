import sys

import pygame

from settings import Settings
from target import Target
from missile import Missile

class ShootDownMissiles:
    """Main class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Shoot Down Missiles!")

        self.target = Target(self)
        self.missile = Missile(self)
        self.missiles = pygame.sprite.Group()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.target.update()
            self._update_missiles()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.target.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.target.moving_left = True
        elif event.key == pygame.K_UP:
            self.target.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.target.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._launch_missile()


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.target.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.target.moving_left = False
        elif event.key == pygame.K_UP:
            self.target.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.target.moving_down = False

    def _launch_missile(self):
        """Create a new missile and add it to the missiles group."""
        new_missile = Missile(self)
        self.missiles.add(new_missile)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for missile in self.missiles.sprites():
            missile.draw_missile()
        self.target.blitme()

        pygame.display.flip()

    def _update_missiles(self):
        """Update position of missiles and get rid of old missiles."""
        self.missiles.update()
        # Get rid of missiles that have disappeared.
        for missile in self.missiles.copy():
            if missile.rect.top > self.settings.screen_height:
                self.missiles.remove(missile)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    sdm = ShootDownMissiles()
    sdm.run_game()
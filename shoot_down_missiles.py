import sys

import pygame

from settings import Settings
from target import Target

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


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
            self.screen.fill(self.settings.bg_color)
            self.target.blitme()

            pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run the game.
    sdm = ShootDownMissiles()
    sdm.run_game()
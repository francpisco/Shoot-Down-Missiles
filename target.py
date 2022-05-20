import pygame

class Target:
    """A class to manage the target."""

    def __init__(self, sdm_game):
        """Initialize the ship and set its starting position."""

        self.screen = sdm_game.screen
        self.settings = sdm_game.settings
        self.screen_rect = sdm_game.screen.get_rect()

        # Load the target image and get its rect.
        self.image = pygame.image.load('images/target.png')
        self.rect = self.image.get_rect()

        # Start each new target at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the target's position based on the movement flag."""
        # Update the ship's position, not the rect.
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.x += self.settings.target_speed
        if self.moving_left and self.rect.centerx > 0:
            self.x -= self.settings.target_speed
        if self.moving_up and self.rect.centery > 0:
            self.y -= self.settings.target_speed
        if self.moving_down and self.rect.centery < self.screen_rect.bottom:
            self.y += self.settings.target_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the target at its current location."""
        self.screen.blit(self.image, self.rect)
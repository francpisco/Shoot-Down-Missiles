

class Settings:
    """A class to store all settings for Shoot Down Missiles."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Target settings
        self.target_speed = 1.5

        # Missile settings
        self.missile_speed = 1.2
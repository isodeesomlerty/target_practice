class Settings:
    """A class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initilize the game's settings."""
        # Screen settings
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.misses_limit = 2

        # How quickly the game speeds up
        self.speedup_scale = 1.5

        # Rectangle settings
        self.rectangle_width = 50
        self.rectangle_height = 200
        self.rectangle_color = (150, 150, 150)

        self.initialize_dynamic_settings


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.rectangle_speed = 1.75

        # rectangle_direction of 1 represents down; -1 represents up.
        self.rectangle_direction = 1


    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.rectangle_speed *= self.speedup_scale
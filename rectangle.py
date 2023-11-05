import pygame

class Rectangle:
    """A class to manage the target rectangle."""

    def __init__(self, tp_game):
        """Create a rectangle object at the top right of the screen."""
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tp_game.settings
        self.color = self.settings.rectangle_color

        # Create a rectangle at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.rectangle_width,
                                self.settings.rectangle_height)
        self.reset_position()

    
    def reset_position(self):
        """
        Reset the rectangle's position to the original position.
        Store the rectangle's vertical position as a float.
        """
        self.rect.topright = (self.screen_rect.right, 
                              (self.screen_rect.top + 1))
        self.y = float(self.rect.y)


    def check_edges(self):
        """Return True if alien is at edge of screen."""
        return ((self.rect.top <= 0) or
                (self.rect.bottom >= self.settings.screen_height))
    

    def update(self):
        """Move the rectangle up and down."""
        self.y += (self.settings.rectangle_speed 
                   * self.settings.rectangle_direction)
        self.rect.y = self.y


    def draw_rectangle(self):
        """Draw the rectangle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
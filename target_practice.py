import sys

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from rectangle import Rectangle

class TargetPractice:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.settings.screen_width = self.screen_rect.width
        self.settings.screen_height = self.screen_rect.height
        pygame.display.set_caption("Target Practice")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.rectangle = Rectangle(self)
        self.bullets = pygame.sprite.Group()

        # Start Target Practice in an inactive state
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_rectangle()

            self._update_screen()
            self.clock.tick(60)

    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            

    def _check_play_button(self, mouse_pos):
        """
        Start a new game when the player clicks Play
         and the game is currently inactive.
         """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            # Reset the game statistics.
            self.stats.reset_stats()
            self.game_active = True

            # Reset the positions of the ship and the rectangle.
            self.rectangle.reset_position()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    
    def _fire_bullet(self):
        """Create a new bullet and add it the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        # Count them as missing the target.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
                self._miss_target()

        # Remove any bullets that have collided with the rectangle-ship.
        bullets_hit = pygame.sprite.spritecollide(self.rectangle, self.bullets, 
                                                  True)
        
        # Increase speed of the ship, bullet and rectangle as each bullet hits.
        for bullet in bullets_hit:
            self.settings.increase_speed()


    def _update_rectangle(self):
        """Check if the rectangle is at an edge, then update positions."""
        self._check_rectangle_edges()
        self.rectangle.update()
    

    def _check_rectangle_edges(self):
        """Respond appropriately if the rectangle has reached an edge."""
        if self.rectangle.check_edges():
            self.settings.rectangle_direction *= -1

    
    def _miss_target(self):
        """Respond to the player missing the target."""
        if self.stats.misses_left > 0:
            # Decrement misses_left.
            self.stats.misses_left -= 1

        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _update_screen(self):
        """Update images on the screen, and flip to t he new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.rectangle.draw_rectangle()

        # Draw the Play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    tp = TargetPractice()
    tp.run_game()
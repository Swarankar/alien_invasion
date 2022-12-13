import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """overall class to manage game sassets and behaviour"""

    def __init__(self):
        
        """initialize the game and create game resources"""
        pygame.init()

        self.settings = Settings()
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        #below is to get width and height of screen
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        #we are assigning value to width and height in our settings module
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height


        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship (self)
        self.bullets = pygame.sprite.Group()

        
    def run_game(self):

        """Start the main loop for the game """

        while True:

            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            

    
    def _check_events(self):
    #watch for keybord and mouse events.
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
             # was added wrom net surfing
                    pygame.quit() 
                    sys.exit()

             #Move the ship
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)


                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

                    
    def _update_screen(self):
        #redrawing the screen during each pass through loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.Creates an illusion to movinf objects
            pygame.display.flip()


    def _check_keydown_events(self,event):
        '''respond to keypress'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
                        
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet()

        
        
            

if __name__ == "__main__":
        # Make the game instance and run the game.
        ai = AlienInvasion()

        ai.run_game()

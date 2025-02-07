import sys
import pygame
from settings import Settings
from rocket import Rocket

class Razzo:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode ((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("RAZZO!")
        self.rocket = Rocket (self) 
        self.bg_color = self.settings.bg_color

    def run_game (self):
        while True:
            self._check_event()         
            self.rocket.move()
            self.screen.fill(self.bg_color)                
            self.rocket.blitme()
            self.clock.tick(60)
            pygame.display.flip()


    def _check_event (self):
         for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
    
    
    def _check_keydown_event(self, event):
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False

if __name__ == "__main__":
    gioco = Razzo()
    gioco.run_game()
import pygame

class Rocket:
    def __init__(self, gioco):
        self.screen = gioco.screen
        self.settings = gioco.settings
        self.screen_rect = gioco.screen.get_rect()
        self.image = pygame.image.load ('images/images.jpeg')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_left = False
        self.moving_right = False



    def move (self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.rocket_speed    
            
            
    def blitme (self):
        self.screen.blit (self.image, self.rect)
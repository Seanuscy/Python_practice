import pygame

class Ship(object):
    def __init__(self, aisettins, screen):
        self.screen = screen
        self.aisettins = aisettins

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.screen_rect.right > self.rect.right:
            self.center += self.aisettins.ship_speed_factor
        elif self.moving_left and self.screen_rect.left < self.rect.left:
            self.center -= self.aisettins.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
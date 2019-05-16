import pygame
import random

screen_width = 1024 
screen_height = 576# Init Screen Height and width

class Player(pygame.sprite.Sprite):
    def __init__(self, location, screen):
        pygame.sprite.Sprite.__init__(self)
        self.startloc = location
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (75,75))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.startloc
        self.rect.height = self.rect.height - 4
        self.rect.width -= 8
        self.mom = 2
        self.rotcount = 0
        self.screen = screen
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self, jump):
        if(self.rect.top + self.mom >= screen_height - self.rect.height):
            self.mom = screen_height - self.rect.top - self.rect.height
        self.jump(jump)
        self.fall()
        self.rotate()

    # Method to do the jump animation
    def jump(self, jump):
        if(jump == 'jump'):
            self.mom = -11
            self.image = pygame.image.load("images/player.png")
            self.image = pygame.transform.scale(self.image, (75,75))
            self.image = self.rot_center(self.image, 55)
            self.rotcount = 0

    # Method to do the falling animation
    def fall(self):
        if(self.rect.top <= screen_height - self.rect.height):
             self.rect.top += self.mom

    # Method to rotate the player
    def rotate(self):
        rotangle = 55 - (7*self.rotcount)
        if(rotangle > -75):
            self.image = pygame.image.load("images/player.png")
            self.image = pygame.transform.scale(self.image, (75,75))
            self.image = self.rot_center(self.image, rotangle)
            self.mom += 2
            self.rotcount += 1
        self.mask = pygame.mask.from_surface(self.image)

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    
    def reset(self):
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (75,75))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.startloc
        self.rect.height = self.rect.height - 4
        self.rect.width -= 8
        self.mom = 2
        self.rotcount = 0
        self.mask = pygame.mask.from_surface(self.image)
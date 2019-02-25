import pygame
import random

screen_width = 1024 
screen_height = 576# Init Screen Height and width

#Create the Pipes
class Pipes(pygame.sprite.Sprite):
    def __init__(self,location, screen):
        super().__init__() 
        #Top Pipe
        self.screen = screen
        self.image = pygame.image.load("images/pipe.png")
        self.image = pygame.transform.scale(self.image, (110,793))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.bottompipe = BottomPipe(self, screen)
        self.completed = False
        self.remove = False
    def draw(self):
        self.screen.blit(self.image, self.rect) #Draw the top
    def update(self):
        self.rect.left -= 8
        if(self.rect.left <= -200):
            self.remove = True

class BottomPipe(pygame.sprite.Sprite):
    def __init__(self, top, screen):
        super().__init__() 
        #Top Pipe
        self.screen = screen
        self.image = pygame.image.load("images/pipe.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale(self.image, (110,793))
        self.rect = self.image.get_rect()
        self.rect.left = top.rect.left
        self.rect.top = top.rect.top + 928
        self.completed = True
        self.remove = False
    def draw(self):
        self.screen.blit(self.image, self.rect) #Draw the top    
    def update(self):
        self.rect.left -= 8
        if(self.rect.left <= -200):
            self.remove = True
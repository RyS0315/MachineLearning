'''
AI solving flappy bird

Created on Jan 24, 2019

@author: Riley E. Stadel

'''
import pygame
import random
import Player
#-------------- Initial variables ---------#
pygame.init()# Start Pygame
clock = pygame.time.Clock()# Create the Clock
clock.tick(1000)# Used to manage how fast the screen updates
screen_width = 1024 
screen_height = 576# Init Screen Height and width
screen = pygame.display.set_mode([screen_width, screen_height])#Create the screen
all_sprites_list = pygame.sprite.Group()#Create all sprites group
pipes_list = pygame.sprite.Group()# Create group for all pipes
player_list = pygame.sprite.Group()# Create group for player

class Game():
    def __init__(self):
        self.done = False# Program is running
        self.game = True# Game is running
        self.replay = False
        self.timer = 0#Init the timer -> Used for time events such as new pipes


class Controller():
    def __init__(self, player):
        self.player = player
        self.timer = 0
    def getcontrol(self, timer):
        if(self.player == 'player'):
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    return 'jump'
                if event.type == pygame.QUIT:
                    return 'quit'
        if(self.player == 'ai'):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
            if not game.game:
                return 'jump'
            elif(game.timer % 5 == 0):
                # Change this to run the ai algorithm to return jump or no jump
                rand = random.randint(0, 1)
                if(rand == 1):
                    return 'jump'
                else:
                    return False    
            return False  

#Create the Background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = (self.image.get_rect())
        self.rect.left, self.rect.top = location    
    def draw(self):
        screen.blit(self.image, self.rect)

#Create the Pipes
class Pipes(pygame.sprite.Sprite):
    def __init__(self,location):
        super().__init__() 
        #Top Pipe
        self.image = pygame.image.load("images/pipe.png")
        self.image = pygame.transform.scale(self.image, (110,793))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    def draw(self):
        screen.blit(self.image, self.rect) #Draw the top
    def update(self):
        self.rect.left -= 8
        if(self.rect.left <= -200):
            pipes_list.remove(self)

class BottomPipe(pygame.sprite.Sprite):
    def __init__(self, top):
        super().__init__() 
        #Top Pipe
        self.image = pygame.image.load("images/pipe.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale(self.image, (110,793))
        self.rect = self.image.get_rect()
        self.rect.left = top.rect.left
        self.rect.top = top.rect.top + 928
    def draw(self):
        screen.blit(self.image, self.rect) #Draw the top    
    def update(self):
        self.rect.left -= 8
        if(self.rect.left <= -200):
            pipes_list.remove(self)

def addPipes():
    piperangetop = -650
    piperangebottom = -450
    pipetop = random.randint(piperangetop, piperangebottom)
    newpipes = Pipes((1024, pipetop))
    pipes_list.add(newpipes)
    bottompipe = BottomPipe(newpipes)
    pipes_list.add(bottompipe)

#---- Initialize entities ----#
bg = Background("images/background.png" , (0,0))
addPipes()
player = Player.Player((200,screen_height/2), screen)
player_list.add(player)
controller = Controller('ai')
game = Game()

def gameOver():
    print("gameover")
    return False

def checkCollision():
    blocks_hit_list = pygame.sprite.spritecollide(player, pipes_list, False, pygame.sprite.collide_mask)
    if(player.rect.top <= 0):
        return gameOver()
    if(player.rect.top + player.rect.height >= screen_height):
        return gameOver()
    for _ in blocks_hit_list:
        return gameOver()
    return True

def drawGameOver(inp, game):
    if(game.replay):
        for i in iter(pipes_list.sprites()):
            pipes_list.remove(i)
        bg.draw()
        player.reset()
        player.draw()
        pygame.display.update()
        if(inp == 'jump'):
            addPipes()
            game.timer = 0
            game.game = True
            game.replay = False
    else:
        if(inp == 'jump'):
            game.replay = True

#---- Run the game ----#
def update(inp):
    player.update(inp)
    pipes_list.update()

def render():
    bg.draw()
    for i in iter(pipes_list.sprites()):
        i.draw()
    player.draw()
    pygame.display.update()

while not game.done:
    inp = controller.getcontrol(game)
    if(inp == 'quit'):
        game.done = True
    if game.game:
        update(inp)
        game.game = checkCollision()
        render()
        if(game.timer == 80):
            addPipes()
            game.timer = 0
        game.timer += 1
    else:
        drawGameOver(inp, game)

pygame.quit()
print("End")
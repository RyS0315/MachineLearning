'''
AI solving flappy bird

Created on Jan 24, 2019

@author: Riley E. Stadel

'''
import pygame
import random
import Player
import DataProcessor as dp
import Pipes
import DataRecorder
#-------------- Initial variables ---------#
pygame.init()# Start Pygame
clock = pygame.time.Clock()# Create the Clock
clock.tick(1000)# Used to manage how fast the screen updates
screen_width = 1024# Init Screen Width
screen_height = 576# Init Screen Height
screen = pygame.display.set_mode([screen_width, screen_height])# Create the screen
all_sprites_list = pygame.sprite.Group()# Create all sprites group
pipes_list = pygame.sprite.Group()# Create group for all pipes
player_list = pygame.sprite.Group()# Create group for player

class Game():
    def __init__(self, player, pipes):
        self.exit = False# Program is running
        self.play = False# Game is running
        self.replay = False
        self.timer = 0# Init the timer -> Used for time events such as new pipes
        self.player = player
        self.pipes = pipes
        self.score = 0

class Controller():
    def __init__(self, player, game):
        self.player = player
        self.timer = 0
        self.processor = dp.DataProcessor(game)
    def getcontrol(self, timer):
        if(self.player == 'player'):
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if game.play:
                        DataRecorder.addNewData(game, 1)
                        DataRecorder.addResults(1)
                    else:
                        DataRecorder.sectioninps = 0
                    return 'jump'
                if event.type == pygame.QUIT:
                    return 'quit'
            if(self.timer % 3 == 0):
                if game.play:
                    DataRecorder.addNewData(game, 0)
                    DataRecorder.addResults(1)
        if(self.player == 'ai'):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 'quit'
            return self.processor.processEvent()            

#Create the Background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)# call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = (self.image.get_rect())
        self.rect.left, self.rect.top = location    
    def draw(self):
        screen.blit(self.image, self.rect)

def addPipes():
    piperangetop = -650
    piperangebottom = -450
    pipetop = random.randint(piperangetop, piperangebottom)
    newpipes = Pipes.Pipes((1024, pipetop), screen)
    pipes_list.add(newpipes)
    pipes_list.add(newpipes.bottompipe)

#---- Initialize entities ----#
bg = Background("images/background.png" , (0,0))
addPipes()
player = Player.Player((200,screen_height/2), screen)
player_list.add(player)
game = Game(player, pipes_list)
controller = Controller('player', game)

def gameOver():
    print("gameover")
    DataRecorder.addResults(0)
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
            game.play = True
            game.replay = False
    else:
        if(inp == 'jump'):
            game.replay = True

def checkPass(player, pipes):
    for pipe in pipes:
        if(pipe.rect.left + pipe.rect.width <= player.rect.left):
            if(pipe.completed):
                continue
            pipe.completed = True
            game.score += 1
            print(game.score)

def checkRemove(pipes):
    for pipe in pipes:
        if(pipe.remove):
            pipes.remove(pipe)
            print('removed')

#---- Run the game ----#
def update(inp):
    player.update(inp)
    pipes_list.update()
    checkPass(player, pipes_list)
    checkRemove(pipes_list)

def render():
    bg.draw()
    for i in iter(pipes_list.sprites()):
        i.draw()
    player.draw()
    pygame.display.update()

while not game.exit:
    inp = controller.getcontrol(game)
    if(inp == 'quit'):
        game.exit = True
    if game.play:
        update(inp)
        game.play = checkCollision()
        render()
        if(game.timer == 80):
            addPipes()
            game.timer = 0
        game.timer += 1
    else:
        drawGameOver(inp, game)

pygame.quit()
print("End")
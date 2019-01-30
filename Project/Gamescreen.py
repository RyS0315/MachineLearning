'''
AI solving flappy bird

Created on Jan 24, 2019

@author: Riley E. Stadel

'''
import pygame
import random
#-------------- Initial variables ---------#
pygame.init()# Start Pygame
clock = pygame.time.Clock()# Create the Clock
clock.tick(1000)# Used to manage how fast the screen updates
screen_width = 1024 
screen_height = 576# Init Screen Height and width
screen = pygame.display.set_mode([screen_width, screen_height])#Create the screen
done = False# Program is running
game = True# Game is running
timer = 0#Init the timer -> Used for time events such as new pipes
all_sprites_list = pygame.sprite.Group()#Create all sprites group
pipes_list = pygame.sprite.Group()# Create group for all pipes
player_list = pygame.sprite.Group()# Create group for player

class Controller():
    def __init__(self, player):
        self.player = player
    def getcontrol(self):
        if(self.player == 'player'):
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    return 'jump'
                if event.type == pygame.QUIT:
                    return 'quit'
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

class Player(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (82,55))
        self.rect = self.image.get_rect()
        # self.rect = pygame.ellipse(self.image, (0,0,0), [0,0,self.rect.width,self.rect.height])
        self.rect.left, self.rect.top = location
        # self.rect.height = self.rect.height - 8
        self.rect.width = self.rect.width / 2
        self.rect.move_ip(200, 0)
        # self.rect.top += 100
        self.mom = 2
        self.rotcount = 0
    def draw(self):
        pygame.draw.rect(screen,(0,0,0), self.rect, 0)
        screen.blit(self.image, self.rect)
    def update(self, jump):
        if(self.rect.top + self.mom >= screen_height - self.rect.height):
            self.mom = screen_height - self.rect.top - self.rect.height
        if(jump == 'jump'):
            self.mom = -13
            self.image = pygame.image.load("images/player.png")
            self.image = pygame.transform.scale(self.image, (75,75))
            self.image = self.rot_center(self.image, 45)
            # self.rect = self.image.get_rect()
            self.rotcount = 0
        if(self.rect.top <= screen_height - self.rect.height):
            self.rect.top += self.mom
        rotangle = 45 - (7*self.rotcount)
        if(rotangle > -75):
            self.image = pygame.image.load("images/player.png")
            self.image = pygame.transform.scale(self.image, (75,75))
            self.image = self.rot_center(self.image, rotangle)
            # self.rect = self.image.get_rect()
            self.mom += 2
            self.rotcount += 1
    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image

#---- Initialize entities ----#
bg = Background("images/background.png" , (0,0))
piperangetop = -650
piperangebottom = -450
pipetop = random.randint(piperangetop, piperangebottom)
player = Player((200,350))
player_list.add(player)
controller = Controller('player')
pipes = Pipes((1024, pipetop))
pipes_list.add(pipes)
bottompipe = BottomPipe(pipes)
pipes_list.add(bottompipe)

def addPipes():
    piperangetop = -650
    piperangebottom = -450
    pipetop = random.randint(piperangetop, piperangebottom)
    newpipes = Pipes((1024, pipetop))
    pipes_list.add(newpipes)
    bottompipe = BottomPipe(newpipes)
    pipes_list.add(bottompipe)

def gameOver():
    print("gameover")
    return False

def checkCollision():
    blocks_hit_list = pygame.sprite.spritecollide(player, pipes_list, False)
    for _ in blocks_hit_list:
        return gameOver()
    return True

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

while not done:
    inp = controller.getcontrol()
    if(inp == 'quit'):
        done = True
    if game:
        update(inp)
        game = checkCollision()
        render()
        if(timer == 80):
            addPipes()
            timer = 0
        timer += 1

pygame.quit()
print("End")
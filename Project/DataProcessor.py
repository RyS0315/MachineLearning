import random
import DataRecorder

class DataProcessor():
    def __init__(self, game):
        self.action = 'jump'
        self.game = game
    def processEvent(self):
        if not self.game.play:
            return 'jump'
        elif(self.game.timer % 5 == 0):
            return self.processData()
    
    def processData(self):
        # Change this to run the ai algorithm to return jump or no jump
            rand = random.randint(0, 1)
            if(rand == 1):
                DataRecorder.formatData(self.game, 1)
                DataRecorder.sectioninps += 1
                return 'jump'
            else:
                DataRecorder.formatData(self.game, 0)
                DataRecorder.sectioninps += 1
                return False
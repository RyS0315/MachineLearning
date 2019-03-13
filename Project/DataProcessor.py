import random
import DataRecorder
import pandas as pd
from sklearn.neural_network import MLPClassifier
import numpy

class DataProcessor():
    def __init__(self, game):
        self.action = 'jump'
        self.game = game
    def processEvent(self):
        if not self.game.play:
            DataRecorder.sectioninps = 0
            self.MLPReader()
            return 'jump'
        elif(self.game.timer % 3 == 0):
            return self.processData()
    
    def processData(self):
        # Remake this algorithm
        data = DataRecorder.formatData(self.game, 1)
        DataRecorder.sectioninps += 1
        predict = self.clf.predict([data])
        if(predict == [1,]):
            DataRecorder.addNewData(self.game, 1)
            print("Predicted Pass with jump")
            return 'jump'
        else:
            print("Predicted fail with jump")
            data = DataRecorder.formatData(self.game, 0)
            predict = self.clf.predict([data])
            if(predict == [1,]):
                DataRecorder.addNewData(self.game, 0)
                print("Predicted Pass with fail")
                return False
        top = self.game.player.rect.top
        rand = random.randint(0, 1)
        if(top > 500):
            DataRecorder.addNewData(self.game, 1)
            print('---Do Jump---')
            return 'jump'
        elif(top < 100):
            DataRecorder.addNewData(self.game, 0)
            print('---Do Nothing---')
            return False
        elif(rand == 1):
            DataRecorder.addNewData(self.game, 1)
            print('---Do Jump---')
            return 'jump'
        else:
            DataRecorder.addNewData(self.game, 0)
            print('---Do Nothing---')
            return False
    def MLPReader(self):
        dfx = pd.read_csv("Data\\DataInputs.csv", 
        names=['ignore', 'play_y', 'pipe_x', 'pipe_y','mom', 'jump'], 
        index_col=None)
        dfy = pd.read_csv("Data\\DataResults.csv", 
                names=['ignore', 'outcome'])

        X = dfx[['play_y', 'pipe_x', 'pipe_y', 'mom','jump']].astype('float').values
        y = dfy[['outcome']].astype('float').values

        y = numpy.ravel(y)
        self.clf = MLPClassifier(hidden_layer_sizes=(128, 64), verbose=False, alpha=.01)
        
        self.clf.fit(X, y)

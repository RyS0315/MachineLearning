import random
import DataRecorder
import pandas as pd
from sklearn.neural_network import MLPClassifier
import numpy
from sklearn.model_selection import StratifiedKFold
# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

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
        dfx = pd.read_csv("Data/DataInputs.csv", 
        names=['ignore', 'play_y', 'pipe_x', 'pipe_y','mom', 'jump'], 
            index_col=None)

        dfy = pd.read_csv("Data/DataResults.csv", 
                names=['ignore', 'outcome'])

        X = dfx[['play_y', 'pipe_x', 'pipe_y', 'mom','jump']].astype('float').values
        y = dfy[['outcome']].astype('float').values
        # y = numpy.ravel(y)

        print(X.shape)

        skf = StratifiedKFold(n_splits = 10)
        skf.get_n_splits(X, y)

        for train_index, test_index in skf.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]


        self.clf = MLPClassifier(hidden_layer_sizes=(256, 128), activation='relu', 
                        solver='adam', alpha=0.0001, batch_size='auto', 
                        learning_rate='constant', learning_rate_init=0.001, 
                        power_t=0.5, max_iter=200, shuffle=True, random_state=None, 
                        tol=0.0001, verbose=False, warm_start=False, momentum=0.9, 
                        nesterovs_momentum=True, early_stopping=False, 
                        validation_fraction=0.1, beta_1=0.9, beta_2=0.999, 
                        epsilon=1e-08)

        self.clf.fit(X_train, y_train)


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
from sklearn.metrics import mean_squared_error

class DataProcessor():
    def __init__(self, game):
        self.action = 'jump'
        self.game = game
        self.bestMSE = 100000
    def processEvent(self):    
        if not self.game.play:
            if not self.game.replay:
                return "jump"
            DataRecorder.sectioninps = 0
            self.MLPReader()
            DataRecorder.addMSE(self.mserecord)
            return 'jump'
        elif(self.game.timer % 2 == 0):
            return self.processData()
    
    def processData(self):
        # top = self.game.player.rect.top  
        # if(top > 500):
        #     DataRecorder.addNewData(self.game, 1)
        #     DataRecorder.addResults(1)
        #     print('---Do Jump---')
        #     return 'jump'
        # elif(top < 100):
        #     DataRecorder.addNewData(self.game, 0)
        #     DataRecorder.addResults(1)
        #     print('---Do Nothing---')
        #     return False
        datapass = DataRecorder.formatData(self.game, 100) #We want to predict a pass with current conditions
        datafail = DataRecorder.formatData(self.game, -100)
        if(datapass[1] < 0):
            DataRecorder.addNewData(self.game, 0)
            DataRecorder.addResults(1)
            return False
        elif(datapass[1] > 75):
            DataRecorder.addNewData(self.game, 1)
            DataRecorder.addResults(1)
            return 'jump'
        else:
            # print(data)
            predictpass = self.bestclf.predict([datapass])# Predict
            predictfail = self.bestclf.predict([datafail])
            
            if(predictpass == [1,]):
                DataRecorder.addNewData(self.game, 1)
                DataRecorder.addResults(1)
                print("Predicted A Jump")
                return 'jump'
            else:
                print("Predicted A No Jump")
                DataRecorder.addNewData(self.game, 0)
                DataRecorder.addResults(1)
                return False
                
        # rand = random.randint(0, 1)
        # if(rand == 1):
        #     data = DataRecorder.formatData(self.game, rand)
        #     DataRecorder.sectioninps += 1
        #     predict = self.clf.predict([data])
        #     if(predict == [1,]):
        #         DataRecorder.addNewData(self.game, 1)
        #         DataRecorder.addResults(1)
        #         print("Predicted Pass with jump")
        #         return 'jump'
        #     else:
        #         print("Predicted fail with jump")
        #         data = DataRecorder.formatData(self.game, 0)
        #         predict = self.clf.predict([data])
        #         if(predict == [1,]):
        #             DataRecorder.addNewData(self.game, 0)
        #             DataRecorder.addResults(1)
        #             print("Predicted Pass with no jump")
        #             return False
        # else:
        #     data = DataRecorder.formatData(self.game, rand)
        #     DataRecorder.sectioninps += 1
        #     predict = self.clf.predict([data])
        #     if(predict == [1,]):
        #         DataRecorder.addNewData(self.game, 0)
        #         DataRecorder.addResults(1)
        #         print("Predicted Pass with no jump")
        #         return False
        #     else:
        #         print("Predicted fail with no jump")
        #         data = DataRecorder.formatData(self.game, 1)
        #         predict = self.clf.predict([data])
        #         if(predict == [1,]):
        #             DataRecorder.addNewData(self.game, 1)
        #             DataRecorder.addResults(1)
        #             print("Predicted Pass jump")
        #             return 'jump'
    def MLPReader(self):
        dfx = pd.read_csv("Data/DataInputs.csv", 
        names=['ignore', 'player_pos', 'pipe_x', 'pipe_y','mom', 'jump'], 
            index_col=None)

        dfy = pd.read_csv("Data/DataResults.csv", 
                names=['ignore', 'outcome'])

        outcome = dfy[['outcome']].astype('float').values
        X = dfx[['pipe_x', 'pipe_y','mom']].astype('float').values
        X = numpy.append(X, outcome, axis=1)
        print(X[0])
        y = dfx[['jump']].astype('float').values
        print(y[0])
        # X = dfx[['play_y', 'pipe_x', 'pipe_y', 'mom','jump']].astype('float').values
        # y = dfy[['outcome']].astype('float').values
        # y = numpy.ravel(y)
        # print(X[0])
        print(X.shape)

        skf = StratifiedKFold(n_splits = 10)
        skf.get_n_splits(X, y)
        it = 0
        bestMSE = 100000
        for train_index, test_index in skf.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]


            clf = MLPClassifier(hidden_layer_sizes=(128, 64, 32), activation='relu', 
                        solver='adam', alpha=0.001, batch_size='auto', 
                        learning_rate='constant', learning_rate_init=0.001, 
                        power_t=0.5, max_iter=200, shuffle=True, random_state=0, 
                        tol=0.0001, verbose=False, warm_start=False, momentum=0.9, 
                        nesterovs_momentum=True, early_stopping=False, 
                        validation_fraction=0.1, beta_1=0.9, beta_2=0.999, 
                        epsilon=1e-08)

            clf.fit(X_train, y_train.ravel())
            predictions = clf.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            print("iteration" + str(it))
            print(mse)
            it += 1
            
            if(mse < bestMSE):
                bestMSE = mse
                self.mserecord = mse
                self.bestclf = clf
                
        


import pandas as pd
from sklearn.neural_network import MLPClassifier

dfx = pd.read_csv("Data\\DataInputs.csv", 
        names=['ignore', 'play_y', 'pipe_x', 'pipe_y', 'jump'], 
        index_col=None)
dfy = pd.read_csv("Data\\DataResults.csv", 
        names=['ignore', 'outcome'])


X = dfx[['play_y', 'pipe_x', 'pipe_y', 'jump']].astype('float').values
y = dfy[['outcome']].astype('float').values

clf = MLPClassifier(hidden_layer_sizes=(128,), verbose=True)

clf.fit(X, y)

print(clf.score(X,y))
print(clf.predict([X[100,:]]))

#After fit, use predict to predict the move


#Pip install Keras
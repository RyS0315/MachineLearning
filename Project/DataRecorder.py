import pandas as pd


def clearFile():
    inputs = "Data/DataInputs.csv"
    results = "Data/DataResults.csv"
    dfy = pd.read_csv("Data/DataResults.csv", 
                names=['ignore', 'outcome'])
    dfx = pd.read_csv("Data/DataInputs.csv", 
        names=['ignore', 'player_pos', 'pipe_x', 'pipe_y','mom', 'jump'], 
            index_col=None)
    y = dfy['outcome']
    y = y[:100]
    y = pd.DataFrame({"Result":y})
    x = dfx[['player_pos', 'pipe_x', 'pipe_y','mom', 'jump']].values
    x = x[:100]

    x = pd.DataFrame(x)
    file = open(inputs, 'w')
    file.truncate()
    file.close()
    with open(inputs, 'a') as f:
            x.to_csv(f, header=False) 
    file = open(results, 'w')
    file.truncate()
    file.close()
    with open(results, 'a') as f:
            y.to_csv(f, header=False) 

def createSection():
    #restart the counter between pipes
    sectioninps = 0

def addData(data):
    file = "Data/DataInputs.csv"
    df = pd.DataFrame(data)
    with open(file, 'a') as f:
        df.to_csv(f, header=False)
    return True

def addResults(result):
    #adds the outcome for the
    file = "Data/DataResults.csv"
    resarr = []
    if(result == 1):
        result = 100
    if(result == 0):
        result = -100
        dfy = pd.read_csv("Data/DataResults.csv", 
                names=['ignore', 'outcome'], index_col=None)
        y = dfy['outcome']
        y = y[:-3]
        y = pd.DataFrame({"Result":y})
        f = open(file, 'w')
        f.truncate()
        f.close()
        with open(file, 'a') as f:
            y.to_csv(f, header=False) 
        for i in range(2):
            resarr.append(result)
    resarr.append(result)
    df = pd.DataFrame({'Result':resarr})
    with open(file, 'a') as f:
        df.to_csv(f, header=False)
    res = pd.read_csv(file)
    # print(res)
    return True

def readInputs():
    file = "Data/DataInputs.csv"
    df = pd.read_csv(file)
    return df

def formatData(game, result):
    for pipe in game.pipes:
        if(not pipe.completed):
            nextPipe = pipe
            break
    pipetop = game.player.rect.top - (nextPipe.rect.top + 793)
    data = {'PlayerPosition': [game.player.rect.top],
          'PipePositionX': [nextPipe.rect.left],
          'PipePositionY': [pipetop],
          'PlayerMom' : [game.player.mom],
          'Input': [result]}
    return [nextPipe.rect.left, pipetop, game.player.mom, result]

def addNewData(game, result):
    for pipe in game.pipes:
        if(not pipe.completed):
            nextPipe = pipe
            break
    pipetop = game.player.rect.top - (nextPipe.rect.top + 793)
    data = {'PlayerPosition': [game.player.rect.top],
          'PipePositionX': [nextPipe.rect.left],
          'PipePositionY': [pipetop],
          'PlayerMom' : [game.player.mom],
          'Input': [result]}
    addData(data)


def addMSE(mse):
    file = "Data/DataMSE.csv"
    data = pd.DataFrame({"MSE": [mse]})
    with open(file, 'a') as f:
        data.to_csv(f, header=False)


def clearMSE():
    f = "Data/DataMSE.csv"
    file = open(f, 'w')
    file.truncate()
    file.close()
clearMSE()
clearFile()
# newdata = formatData()
# addDatas(newdata)
# readInputs()
import pandas as pd
sectioninps = 0

def clearFile():
    file = open("Data/DataInputs.csv", 'w')
    file.truncate()
    file.close()
    file = open("Data/DataResults.csv", 'w')
    file.truncate()
    file.close()

def createSection():
    #restart the counter between pipes
    sectioninps = 0

def addData(data):
    file = "Data/DataInputs.csv"
    df = pd.DataFrame(data)
    with open(file, 'a') as f:
        df.to_csv(f, header=False)
    return True

def addResults(result, numinps):
    #adds the outcome for the
    file = "Data/DataResults.csv"
    resarr = []
    for i in range(0, numinps-1):
        resarr.append(result)
    df = pd.DataFrame({'Result':resarr})
    with open(file, 'a') as f:
        df.to_csv(f, header=False)
    res = pd.read_csv("Data/DataResults.csv")
    readInputs()
    print(res)
    sectioninps = 0
    return True

def readInputs():
    file = "Data/DataInputs.csv"
    df = pd.read_csv(file)
    print(df)
    return df

def formatData(game, result):
    for pipe in game.pipes:
        if(not pipe.completed):
            nextPipe = pipe
    data = {'PlayerPosition': [game.player.rect.left],
          'PipePositionX': [nextPipe.rect.left],
          'PipePositionY': [nextPipe.rect.top],
          'Input': [result]}
    addData(data)

# newdata = formatData()
# addDatas(newdata)
# readInputs()
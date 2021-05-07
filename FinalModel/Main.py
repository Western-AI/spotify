from FinalModels.ModelMaking.ModelCreatorMain import ModelCreatorMain
from FinalModels.FinishedModels.runningFinishedModels import runningFinishedModels

class Main:
        #running Class
        #To use the finished models in FinishedModels folder0
    def CreateModel (self,modelNumber, dataFile=""):# if from another Data file use dataFile
        if modelNumber == 0:
            ModelCreatorMain(modelNumber, dataFile)
        else:
            print("Model not in range")
    def PredictValues (self,modelNumber, inputData): # inputData as ['acousticness', 'danceability', 'energy', 'explicit',
                                                     # 'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
                                                     # 'speechiness', 'tempo', 'valence', 'year']
        runningFinishedModels(modelNumber, inputData)

    def __init__(self):
            pass



            # if from another Data file use dataFile
        #to use existing mdoel with input data
            #makeModel= False
            #input data = Data in order

        #Modelnumber = int
            #O = Adding summs method



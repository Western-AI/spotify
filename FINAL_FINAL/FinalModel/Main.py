from FinalModels.ModelMaking.ModelCreatorMain import ModelCreatorMain
from FinalModels.FinishedModels.runningFinishedModels import runningFinishedModels
import random
import matplotlib.pyplot as plt
plt.style.use('bmh')


class Main:
    # running Class
    # To use the finished models in FinishedModels folder0
    def CreateModel(self, modelNumber, dataFile=""):  # if from another Data file use dataFile
        ModelCreatorMain(modelNumber, dataFile)

    def PredictValues(self, modelNumber,
                      inputData):  # inputData as ['acousticness', 'danceability', 'energy', 'explicit',
        # 'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
        # 'speechiness', 'tempo', 'valence', 'year']
        run = runningFinishedModels(modelNumber, inputData)
        val = run.Predict_val
        run = None
        return val

    def makegraph (self):
        boo = ModelCreatorMain(-2, file_loc="")
        rest = boo.graph_Val

        run = runningFinishedModels(-2, [0])
        equation = run.graph_vals

        ModelCreatorMain
        plt.title('Model')
        plt.xlabel('Summing model: Summed values', fontsize=18)
        plt.ylabel('Popularity', fontsize=18)
        plt.scatter(rest[0],rest[1])
        plt.scatter(equation[0], equation[1])

        plt.show()

    def __init__(self):
        pass

    def grabRealSong(self, modelnum):
        hi = ModelCreatorMain(-1, file_loc="")
        val = random.randint(0, 100000)
        x_ran, y_ran = hi.grabSong(val)
        y_pre = self.PredictValues(modelnum, x_ran)
        return [y_ran, y_pre]

        # if from another Data file use dataFile
        # to use existing mdoel with input data
        # makeModel= False
        # input data = Data in order

        # Modelnumber = int
        # O = Adding summs method

from FinalModels.ModelMaking.DataPreProcessing import DataPreProcessing
from FinalModels.ModelMaking.SummingModel import sumingModel
from FinalModels.ModelMaking.AllPolyModel import AllPolyModel


class ModelCreatorMain:
    def grabSong(self, val):
        return self.x[val], self.y[val]

    def __init__(self, modelNumber, file_loc):

        if file_loc == "":
            file_loc = "Data/data.csv"
        pre = DataPreProcessing(file_loc)
        self.x, self.y = pre.getDataAsXY()
        pre = None
        if modelNumber == 0:
            sumingModel(self.x, self.y)
        elif modelNumber == 1:
            AllPolyModel(self.x, self.y)
        elif modelNumber == -1:
            pass
        elif modelNumber==-2:
            hi = sumingModel(self.x,self.y)
            self.graph_Val= hi.graph()
        else:
            print("Model not in range")

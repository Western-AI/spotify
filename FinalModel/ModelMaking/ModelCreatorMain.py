from FinalModels.ModelMaking.DataPreProcessing import DataPreProcessing
from FinalModels.ModelMaking.SummingModel import sumingModel

class ModelCreatorMain:
    def __init__(self,modelNumber,file_loc):

        if file_loc == "":
            file_loc = "Data/data.csv"
        pre = DataPreProcessing(file_loc)
        x,y = pre.getDataAsXY()
        pre=None
        if modelNumber==0:
            sumingModel(x,y)
        else:
             print("Model not in range")



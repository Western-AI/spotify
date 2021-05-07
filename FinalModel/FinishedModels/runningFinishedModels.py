import numpy as np

from FinalModels.FinishedModels.predictingUsing_SummingModel import predictingUsing_SummingModel


class runningFinishedModels:

    def __init__(self, modelnumber,inputData):
        if modelnumber == 0:
            model = predictingUsing_SummingModel(inputData)
        else:
            print("Model does Not exist")


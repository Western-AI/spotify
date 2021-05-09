import numpy as np

from FinalModels.FinishedModels.predictingUsing_AllPolyModel import predictingUsing_AllPolyModel
from FinalModels.FinishedModels.predictingUsing_SummingModel import predictingUsing_SummingModel


class runningFinishedModels:

    def __init__(self, modelnumber,inputData):
        if modelnumber == 0:
            model = predictingUsing_SummingModel(inputData)
            self.Predict_val = model.predicted_val
        elif modelnumber==1:
            model = predictingUsing_AllPolyModel(inputData)
            self.Predict_val = model.predicted_val
        elif modelnumber == -2:
            model = predictingUsing_SummingModel([64.3,  85.2,  51.7,   0.,    2.64, 45.,    8.09, 84.,    0.,    5.34,
                            26.,   95., 0.])
            self.graph_vals= model.makegraph()
        else:
            print("Model does Not exist")


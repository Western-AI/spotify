import numpy as np

from FinalModels.FinishedModels.Equation import toArray, Equation


class predictingUsing_AllPolyModel():


    def __init__(self,inputData):
        self.inputData = np.array(inputData)
        #info_file = open("./FinishedModels/ModelEquations/AllPolyModelEquation.txt","r")
        info_file = open("./FinishedModels/ModelEquations/AllPolyModelEquation.txt", "r")
        text = info_file.read()
        info_file.close()
        powers_equ = toArray(text[2:text.index("s:")])
        slopes_Equ = toArray(text[text.index("s:") + 2:text.index("i:")])
        intercept_Equ = float(text[text.index("i:") + 2:text.index("r")])
        r_sq_Equ = float(text[text.index("r:") + 2:])
        equation = Equation(powers_equ, slopes_Equ, intercept_Equ)
        self.predicted_val = equation.applyEquation(self.inputData)



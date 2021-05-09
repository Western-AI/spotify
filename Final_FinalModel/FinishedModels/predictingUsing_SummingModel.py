import numpy as np

from FinalModels.FinishedModels.Equation import toArray, Equation


class predictingUsing_SummingModel():
    def suming(self):
        index =0
        for co in self.Coeff_:
            self.inputData[index] *= co
            index += 1
        x_new = self.inputData.sum()
        return x_new

    def makegraph(self):
        x = np.arange(-10,60)
        y = []
        for val in x:
            y.append(self.equation.applyEquation(val))
        return [x,y]

    def __init__(self, inputData):
        self.inputData = np.array(inputData)
        coeff_file = open("./FinishedModels/ModelEquations/SummingModelCoeff.txt", "r")
        text = coeff_file.read()
        coeff_file.close()
        #print(text)
        self.Coeff_ = toArray(text[:text.index("r:")])
        r_sq_Coeff = float(text[text.index("r:")+2:])
        x_new = self.suming()
        f = open("./FinishedModels/ModelEquations/SummingModelEquation.txt", "r")
        text = f.read()
        powers_equ = toArray(text[2:text.index("s:")])
        slopes_Equ = toArray(text[text.index("s:")+2:text.index("i:")])
        intercept_Equ = float(text[text.index("i:")+2:text.index("r")])
        r_sq_Equ = float(text[text.index("r:")+2:])
        f.close()
        self.equation = Equation(powers_equ,slopes_Equ,intercept_Equ)
        self.predicted_val = self.equation.applyEquation(x_new)
        #print("predict:", self.predicted_val)
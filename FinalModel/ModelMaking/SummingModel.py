from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np


########################################################################################################################
class LinRegModel:
    def predicting(self, x_p):
        perdicts = []
        trans = self.transformer[1, :]
        perdicts.append(self.model.predict(self.transformer))

        return perdicts

    def run(self, deg):
        # transfor data
        self.transformer = PolynomialFeatures(degree=deg, include_bias=False)
        self.transformer.fit(self.xf)
        self.powers__ = self.transformer.powers_
        x_r = self.transformer.transform(self.xf)
        self.model = LinearRegression().fit(x_r, self.yf)
        r_sq = self.model.score(x_r, self.yf)
        self.deg = deg
        return r_sq, self.model

    def __init__(self, x_, y_):
        self.xf = x_.reshape((-1, 1))
        self.yf = y_
        deg = 1
        while True:
            if deg == 1:
                r1, model1 = self.run(deg)
            r2, model2 = self.run(deg + 1)
            if r2 - r1 < .00001 or r1 > r2:
                self.model = model2
                self.r_sq = r2
                break
            r1 = max(r1, r2)
            if r1 == r2:
                model1 = model2
            deg = deg + 1
        # print('coefficient of determination:', r_sq)


########################################################################################################################
class coeffienctsFinding:  # makes a regression model to find coefficients

    def suming(self, x):
        index = 0
        print(type(x), "\n", x)
        for co in self.slopes:
            x[:, index] *= co
            index += 1
        x_new = x.sum(axis=1)
        return x_new

    def __init__(self, x, y):
        model = LinearRegression().fit(x, y)
        self.slopes = model.coef_
        self.r_sq = model.score(x, y)
        # print('Coeffienct Model complete:', 'r_sq:', model.score(x, y), "\n intercepts: ", model.intercept_, "\n slopes: ",
    #       self.slopes)
    # print("\n\n")


########################################################################################################################
########################################################################################################################
class sumingModel:
    def __init__(self, x, y):
        coeff = coeffienctsFinding(x, y)

        f = open("./FinishedModels/ModelEquations/SummingModelCoeff.txt","w")
        f.write(str(coeff.slopes))
        f.write("\n r:")
        f.write(str(coeff.r_sq))
        f.close()

        x_final = coeff.suming(x)

        coeff = None

        model = LinRegModel(x_final, y)
        powers = model.powers__
        slopes = model.model.coef_
        intercept = model.model.intercept_


        f = open("./FinishedModels/ModelEquations/SummingModelEquation.txt", "w")
        f.write("p:")
        f.write(str(powers))
        f.write("\n s:")
        f.write(str(slopes))
        f.write("\n i:")
        f.write(str(intercept))
        f.write("\n r:")
        f.write(str(model.r_sq))
        f.close()

        model = None
        powers = None
        slopes = None


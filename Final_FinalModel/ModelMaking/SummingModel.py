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
        transformer = PolynomialFeatures(degree=deg, include_bias=False)
        transformer.fit(self.xf)
        powers__ = transformer.powers_
        x_r = transformer.transform(self.xf)
        model = LinearRegression().fit(x_r, self.yf)
        r_sq = model.score(x_r, self.yf)
        return r_sq, model, powers__

    def __init__(self, x_, y_):
        self.xf = x_.reshape((-1, 1))
        self.yf = y_
        deg = 1
        self.r_sq, self.model, self.powers_ = self.run(deg)
        while True:
            try:
                r1, model1, powers = self.run(deg + 1)
            except:
                print("can't go any higher")
            if self.r_sq > r1:
                break
            if r1 - self.r_sq < .0001:
                self.model = model1
                self.r_sq = r1
                self.powers_ = powers
                break
                self.powers_ = powers
            self.model = model1
            self.r_sq = r1
            self.powers_ = powers
            deg = deg + 1
        # print('coefficient of determination:', r_sq)


########################################################################################################################
class coeffienctsFinding:  # makes a regression model to find coefficients

    def suming(self, x):
        index = 0
        #print(type(x), "\n", x)
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
    def graph(self):
        return [self.x_final, self.y]

    def __init__(self, x, y):
        coeff = coeffienctsFinding(x, y)

        f = open("./FinishedModels/ModelEquations/SummingModelCoeff.txt","w")
        f.write(str(coeff.slopes))
        f.write("\n r:")
        f.write(str(coeff.r_sq))
        f.close()

        self.x_final = coeff.suming(x)
        self.y = y
        coeff = None

        model = LinRegModel(self.x_final, y)
        powers = model.powers_
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
        self.x_final

        x_final=None
        model = None
        powers = None
        slopes = None
        intercept =None


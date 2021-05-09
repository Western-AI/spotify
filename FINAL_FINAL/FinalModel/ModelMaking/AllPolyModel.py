from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
class AllPolyModel:
    def run(self, deg):
        # transfor data
        #transformer = PolynomialFeatures(degree=deg, include_bias=False).fit_transform(self.x_)
        transformer =PolynomialFeatures(degree=deg,include_bias=False)
        transformer.fit(self.x_)
        x_new = transformer.transform(self.x_)
        model = LinearRegression().fit(x_new, self.y_)
        powers = transformer.powers_
        r_sq = model.score(x_new, self.y_)
        #print('coefficient of determination:', r_sq)
        #print('intercept:', model.intercept_)
        #print('slope:', model.coef_)
        return r_sq, model, powers

    def __init__(self,x,y):
        self.y_ = y
        self.x_ = x
        deg = 2
        self.r_sq, self.model, self.powers_ = self.run(deg)
        while True:
            try:
                r1, model1,powers = self.run(deg + 1)
            except Exception as e:
                print("can't go any higher",e)
            if self.r_sq > r1:
                break
            if r1 - self.r_sq < .001:
                self.model = model1
                self.r_sq = r1
                self.powers_ = powers
                break
            self.model = model1
            self.r_sq = r1
            self.powers_ = powers
            deg = deg + 1
        np.set_printoptions(threshold=np.inf)

        f = open("./FinishedModels/ModelEquations/AllPolyModelEquation.txt", "w")
        f.write("p:")
        f.write(str(self.powers_))
        f.write("\n s:")
        f.write(str(self.model.coef_))
        f.write("\n i:")
        f.write(str(self.model.intercept_))
        f.write("\n r:")
        f.write(str(self.r_sq))
        f.close()
        print("done")


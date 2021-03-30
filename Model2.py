import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
plt.style.use('bmh')

class run:
    def makeModel(self, deg):
        x_ = PolynomialFeatures(degree=deg,include_bias=False).fit_transform(x)
        model = LinearRegression().fit(x_, y)
        r_sq = model.score(x_, y)
        return r_sq,model

    def finddeg (self):
        while True:
            r1, model1 =self.makeModel(deg=self.deg)
            r2, model2 = self.makeModel(deg=self.deg+1)
            if r2-r1<.00001:
                self.model = model2
                self.r_sq = r2
                break
            self.deg=self.deg+1

    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.deg =1




data = pd.read_csv("Resources/archive1/data.csv")

data.drop_duplicates()
data.dropna()

#data = data.head(100)

y = data["popularity"].tolist()
y = np.array(y)

data = data.drop(["artists", "id", "name", "release_date","popularity", "key","duration_ms","mode"], axis=1)

x = np.array(data)
col = list(data.columns)
file = open("modelrun.csv","w")
file.write("column,r_sq,intercept,slope\n")

for co in col:
    x= np.array(data[co].tolist()).reshape(-1,1)
    model = run(y,x)
    model.finddeg()
    slopes = list(np.array(model.model.coef_).flat)
    file.write( "{},{},{},{}\n".format(co,model.r_sq,model.model.intercept_,slopes))
    print("{},{},{},{}\n".format(co,model.r_sq,model.model.intercept_,slopes))
file.close()

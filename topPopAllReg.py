import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
def run(deg):
    transformer = PolynomialFeatures(degree=deg, include_bias=False).fit_transform(x)
    model = LinearRegression().fit(transformer, y)
    r_sq = model.score(transformer, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_,"\n\n\n\n\n")
    return r_sq,model
# constants

#deg =2 coefficient of determination: 0.5197856438141792
# deg = 3 coefficient of determination: 0.5929112767701978
# deg = 4 coefficient of determination: 0.6063151835496412

# data set up
data = pd.read_csv("Resources/archive1/data2.csv")

data.drop_duplicates()
data.dropna()

data = data.head(10000)#133485

y = data["popularity"].tolist()
y = np.array(y)

data = data.drop(["artists", "id", "name", "release_date", "popularity","key","duration_ms","mode"], axis=1)

x = np.array(data)
deg =2
# transfor data
model1 =0
while True:
    print("deg: ", deg)
    if (model1==0):
        r1, model1 = run(deg)
    r2, model2 = run(deg + 1)
    if r2 - r1 < .00001:
        model = model2
        r_sq = r2
        break
    r1,model1 = r2,model2
    deg = deg + 1
print("\n\n\n","-"*40,
      "deg: ", deg)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
# predict response
#y_pred = model.predict(transformer)

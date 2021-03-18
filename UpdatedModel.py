import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# constants
deg = 2

# data set up
data = pd.read_csv("Resources/archive1/data.csv")

data.drop_duplicates()
data.dropna()

#data = data.head(10)

y = data["popularity"].tolist()
y = np.array(y)

data = data.drop(["artists", "id", "name", "release_date", "popularity","key","duration_ms","mode"], axis=1)
#print(data.dtypes)
x = np.array(data)

# transfor data
transformer = PolynomialFeatures(degree=deg, include_bias=False).fit_transform(x)
model = LinearRegression().fit(transformer,y)
r_sq = model.score(transformer, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

# predict response
y_pred = model.predict(transformer)

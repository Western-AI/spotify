import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# constants
deg = 4

# data set up
data = pd.read_csv("Resources/archive1/data.csv")
data.drop_duplicates()
data.dropna()

data = data.head(100)

y = data["popularity"].tolist()
y = np.array(y)

data = data.drop(["artists", "id", "name", "release_date", "popularity"], axis=1)
x = np.array(data)

# transfor data
transformer = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)
model = LinearRegression().fit(x,y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)


# predict response
#y_pred = model.predict(x)
#print('predicted response:', y_pred, sep='\n')
#print("actual", y, sep="\n")
#percentOff=[]
#for i in range(0,len(y)):
#    percentOff.append(round(1000*abs(y_pred[i]-y[i]))/1000)
    #percentOff.append(abs(y_pred[i] - y[i]))
#print("percent off", percentOff, sep="\t")

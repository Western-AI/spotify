import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def run(deg):
    transformer = PolynomialFeatures(degree=deg).fit_transform(x)
    model = LinearRegression().fit(transformer, y)
    r_sq = model.score(transformer, y)
    print('coefficient of determination:', r_sq)
    print('intercept:', model.intercept_)
    print('slope:', model.coef_,"\n\n\n\n\n")
    return r_sq,model


#reading file
data = pd.read_csv("Resources/archive1/data.csv")
#data.inplace = True

data = data[["popularity",	"acousticness",	"danceability",	"energy",	"instrumentalness",	"liveness", "loudness",	"speechiness", "mode"]]
for col in ["acousticness",	"danceability",	"energy",	"instrumentalness",	"liveness",	"speechiness","mode"]:
    data[col] = 100*(data[col])
    data[col] = data[col].astype(int)

data["popularity"] = data["popularity"].astype(int)
print(data)
index = 0
zero =[]
for val in data["popularity"].tolist():
    if val ==0:
       zero.append(index)
    index=index+1

data = data.drop(zero)

print(data)
data = data.drop_duplicates()
data = data.dropna()

#### After this point it is model running
print(data)
size = 10
list_of_models =[]
maxDeg=1
list_of_slopes =[]
list_of_R_sq = []
list_of_dfs = [data.loc[i:i+size-1,:] for i in range(0, len(data),size)]

for df in list_of_dfs:
    print(df)
    df.columns = ["popularity",	"acousticness",	"danceability",	"energy",	"instrumentalness",	"liveness", "loudness",	"speechiness", "mode"]

    print(df)
    y = df["popularity"].tolist()
    y = np.array(y)
#popularity	acousticness	danceability	energy	explicit	instrumentalness	liveness	loudness	speechiness	tempo	valence	year

    #data = data.drop(["artists", "id", "name", "release_date", "popularity","key","duration_ms","mode","explicit"], axis=1)
    dat = df.drop(["popularity"],axis=1)
    i=0
    x = np.array(dat)
    deg =2
    model1 = 0
    while True:
        print("deg: ", deg)
        if (model1==0):
            r1, model1 = run(deg)
        r2, model2 = run(deg + 1)
        deg = deg + 1
        if r2 - r1 < .0001:
            model = model2
            r_sq = r2
            break
        r1,model1 = r2,model2

    print("\n\n\n","-"*40,
      "\ndeg: ", deg)
    print('coefficient of determination:', r_sq)
    print("run: ", i)
    slopes = str(list(np.array(model.coef_).flat))
    slopes = slopes[1:len(slopes) - 1]
    list_of_models.append(model)
    list_of_R_sq.append(r_sq)
    print('intercept:', model.intercept_)
    print('slope:', slopes)
    #file.write("{},{},{},{},{}\n".format(i, r_sq, deg, model.intercept_, slopes))
    i =i+1

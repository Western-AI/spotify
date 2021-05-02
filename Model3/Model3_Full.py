import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


########################################################################################################################
class LinRegModel:
    def run(self,deg):
        # transfor data
        transformer = PolynomialFeatures(degree=deg, include_bias=True).fit_transform(self.xf)
        model = LinearRegression().fit(transformer, self.yf)
        r_sq = model.score(transformer, self.yf)
        print("Deg: ", deg)
        print('coefficient of determination:', r_sq)
        print('intercept:', model.intercept_)
        print('slope:', model.coef_)
        print("\n\n")
        #print("score")
        return r_sq, model

    def __init__(self, x_, y_):
        print("\n\n\n","=" * 100, '\nFinal model Class opened\n', "-" * 100, '\n')
        self.xf=x_.reshape((-1,1))
        self.yf = y_
        print("x : ", self.xf)
        deg = 1
        while True:
            if deg == 1:
                r1, model1 = self.run(deg)
            r2, model2 = self.run(deg + 1)
            if r2 - r1 < .00001:
                model = model2
                r_sq = r2
                break
            r1 = max(r1,r2)
            if r1==r2:
                model1 = model2
            deg = deg + 1
        print('coefficient of determination:', r_sq)


########################################################################################################################
class coeffienctsFinding2:  # makes a regression model to find coefficients
    """Deg:  7
    coefficient of determination: 0.29428903434457265
    intercept: 7.250967892164496
    slope: [ 0.00000000e+00  7.70908958e-01 -2.64276182e-02  2.56927799e-04 6.14927263e-06 -1.38077415e-07  9.47419763e-10 -2.19602114e-12]
    """
    def suming(self, x_t):
        print("\n\n", "-" * 40, " summing process ", "-" * 40)
        index = 0
        print("\n\nbefore ", x_t)
        for co in self.slopes:
            x[:, index] *= co
            index += 1
        print("\nSlopes* values ", x_t)
        x_new = x.sum(axis=1)
        print("\nFinal terms ", x_new)
        return x_new

    def getSlopes(self):
        print("\n\n", "-" * 100, "\nPre process Class closing\n", "=" * 100, "\n")
        return self.slopes

    def __init__(self, x_n, y_n):
        print("=" * 100, '\ncoefficientFinding 2 Class opened\n', "-" * 100, '\n')
        print(x_n.shape)
        print(y_n.shape)
        self.slopes = []
        self.intercept = []
        for colum in range(0,x_n.shape[1]):
            x_y = x_n[:,colum]
            x_y = x_y.reshape(-1,1)
            model = LinearRegression().fit(x_y, y_n)
            self.slopes.append(model.coef_)
            self.intercept.append(model.intercept_)
        #print('Model complete:', 'r_sq:', model.score(x_n, y_n), "\n intercepts: ", model.intercept_, "\n slopes: ",
            #  self.slopes)

        print("\n\n")


########################################################################################################################


class coeffienctsFinding:  # makes a regression model to find coefficients
    """
    Deg:  9
    coefficient of determination: 0.3934636026049614
    intercept: 8.654803106668382
    slope: [ 0.00000000e+00  3.70975720e-01  1.52078082e-02  5.22991399e-03
    -1.38826720e-04 -1.50659477e-05  9.62792559e-07 -2.34509410e-08
    2.75019152e-10 -1.30279121e-12]
    """

    def suming(self, x):
        print("\n\n", "-" * 40, " summing process ", "-" * 40)
        index = 0
        print("\n\nbefore ", x)
        for co in self.slopes:
            x[:, index] *= co
            index += 1
        print("\nSlopes* values ", x)
        x_new = x.sum(axis=1)
        print("\nFinal terms ", x_new)
        return x_new

    def getSlopes(self):
        print("\n\n", "-" * 100, "\nPre process Class closing\n", "=" * 100, "\n")
        return self.slopes

    def __init__(self, x, y):
        print("=" * 100, '\ncoefficientFinding Class opened\n', "-" * 100, '\n')
        print(x.shape)
        print(y.shape)
        model = LinearRegression().fit(x, y)
        self.slopes = model.coef_
        print('Model complete:', 'r_sq:', model.score(x, y), "\n intercepts: ", model.intercept_, "\n slopes: ",
              self.slopes)

        print("\n\n")


########################################################################################################################
class DataPreProcessing:  # to Get data from CSV by panadas, then convert to numpy array and balance all the values

    def drops(self, data):  # For all the columns dropped
        data = data.drop_duplicates()
        data = data.dropna()
        data = data.drop(["artists", "id", "name", "release_date", "duration_ms"], axis=1)
        # 19 columns in data - 5 dropped for being unusable values = 14 columns that are usable
        return data

    def getDataAsXY(self, ):  # to get the final data out as numpy arrays of x and y
        print("\n\n", "-" * 40, " final ", "-" * 40)
        print(self.data)
        y = self.data["popularity"].tolist()
        y = np.array(y)
        print("\n\ny: ", y)
        x = self.data.drop(["popularity"], axis=1)
        x = np.array(x)
        print("\n")
        print("x:", x)
        print("\n\n", "-" * 100, "\nPre process Class closing\n", "=" * 100, "\n")
        return x, y

    def balance(self, df):  # All columns are out of 100 and are ints (to save space and even things out)
        # 10 columns have a range of 0 - 1 soo * 100 to be out of 100 and turned to an int
        for col in ["acousticness", "valence", "danceability", "energy", "instrumentalness", "liveness", "speechiness",
                    "mode", "explicit"]:
            df[col] = df[col] * 100
            # df[col] = df[col].astype(int)

        # removes all rows where popularity = 0 and loudness above the range of -60 to 0, also If temp =0 it gets removed
        df = df.reset_index(drop=True)
        index = 0
        zero = []
        for val in df["popularity"].tolist():
            if val == 0:
                zero.append(index)
            index = index + 1
        index = 0
        for val in df["loudness"].tolist():
            if val > 0:
                zero.append(index)
            index = index + 1
        index = 0
        for val in df["tempo"].tolist():
            if val == 0:
                zero.append(index)
            index = index + 1
        df = df.drop(zero)

        df = df.reset_index(drop=True)

        # remain 4 columns get their range done
        for item in ["year", "key", "loudness", "tempo"]:
            list = df[item].tolist()
            Max = max(list)
            Min = min(list)
            range = Max - Min
            df[item] = df[item] - Min
            df[item] = (df[item] / range) * 100
            df[item] = df[item].fillna(0)
            df[item] = df[item].astype(int)
        return df

    def __init__(self, fileLocation):
        print("=" * 100, '\nPre process Class opened\n', "-" * 100, '\n')
        self.data = pd.read_csv(fileLocation)
        print(self.data)
        self.data = self.drops(self.data)
        self.data = self.balance(self.data)


########################################################################################################################
file = "Data/data.csv"
print("\n\n\nstart\n")
pre = DataPreProcessing(file)
x, y = pre.getDataAsXY()
pre = None
coeff = coeffienctsFinding(x, y)
coeffiencts = coeff.getSlopes()
x_final = coeff.suming(x)
print('\n\nx terms ',x_final)
Model = LinRegModel(x_final,y)
coeff = None

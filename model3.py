
import pandas as pd
import numpy as np


class DataPreProcessing: # to Get data from CSV by panadas, then convert to numpy array and balance all the values

    def drops (self,data):
        data = data.drop_duplicates()
        data = data.dropna()
        data = data.drop(["artists", "id", "name", "release_date", "duration_ms"], axis=1) # there 19 -5 = 14
        return data

    def balance (self,data):
        for col in ["acousticness", "valence" "danceability", "energy", "instrumentalness", "liveness", "speechiness", "mode", "popularity", "explicit"]: #10
            data[col] = 100 * (data[col])
            data[col] = data[col].astype(int)

            #year , key, loudness, tempo
        index = 0
        zero = []
        for val in data["popularity"].tolist():
            if val == 0:
                zero.append(index)
            index = index + 1
        index =0
        for val in data["loudness"].tolist():
            if val > 0:
                zero.append(index)
            index = index + 1

        data = data.drop(zero)

        for item in ["year", "key","loudness","tempo"]:
            list = data[item].tolist()
            max = max(list)
            list = min(list)

        return data

    def __init__(self, filelLocation):
        print('Pre process Class opened\n')
        self.data = pd.read_csv(filelLocation)
        self.data = self.drops(self.data)
        print(self.data)

file = "Data/data.csv"
print("\n\n\nstart\n")
pre = DataPreProcessing(file)

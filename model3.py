########################################################################################################################
class DataPreProcessing: # to Get data from CSV by panadas, then convert to numpy array and balance all the values

    def drops (self,data): # For all the columns dropped
        data = data.drop_duplicates()
        data = data.dropna()
        data = data.drop(["artists", "id", "name", "release_date", "duration_ms"], axis=1)
        # 19 columns in data - 5 dropped for being unusable values = 14 columns that are usable
        return data

    def getDataAsXY (self, ):# to get the final data out as numpy arrays of x and y 
        print("\n\n","-" *40," final ", "-" *40)
        print(self.data)
        y = self.data["popularity"].tolist()
        y = np.array(y)
        print("\n\ny: ", y)
        x= self.data.drop(["popularity"],axis=1)
        print("\n")
        print("x:", x)
        print("\n\n","-"*100,"\nPre process Class closing\n","="*100,"\n")
        return x,y

    def balance (self, df): # All columns are out of 100 and are ints (to save space and even things out)
        # 10 columns have a range of 0 - 1 soo * 100 to be out of 100 and turned to an int
        for col in ["acousticness", "valence", "danceability", "energy", "instrumentalness", "liveness","speechiness", "mode", "explicit"]:
            df[col] = df[col] * 100
            df[col] = df[col].astype(int)

        # removes all rows where popularity = 0 and loudness above the range of -60 to 0, also If temp =0 it gets removed
        df = df.reset_index(drop=True)
        index = 0
        zero = []
        for val in df["popularity"].tolist():
            if val == 0:
                zero.append(index)
            index = index + 1
        index =0
        for val in df["loudness"].tolist():
            if val > 0:
                zero.append(index)
            index = index + 1
        index =0
        for val in df["tempo"].tolist():
            if val == 0:
                zero.append(index)
            index = index + 1
        df = df.drop(zero)

        df = df.reset_index(drop=True)

        # remain 4 columns get their range done
        for item in ["year", "key","loudness","tempo"]:
            list = df[item].tolist()
            Max = max(list)
            Min = min(list)
            range = Max-Min
            for col in ["year", "key","loudness","tempo"]:
                df[col] = ((df[col] - Min) / range) * 100
                df[col] = df[col].astype(int)
        return df

    def __init__(self, fileLocation):
        print("="*100,'\nPre process Class opened\n', "-"*100,'\n')
        self.data = pd.read_csv(fileLocation)
        print(self.data)
        self.data = self.drops(self.data)
        self.data = self.balance(self.data)


file = "Data/data.csv"
print("\n\n\nstart\n")
pre = DataPreProcessing(file)
x,y = pre.getDataAsXY()
pre= None

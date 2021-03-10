"""
@Creator Gunveer V,
Takes a database of spotify tracks and determines whether a set of given attributes will make a track "popular"
Only takes acousticness so far
"""

#beginning
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')

#store
data = pd.read_csv("data.csv")

#attributes = ['acousticness', 'danceability', 'energy', 'liveness', 'popularity' , 'speechiness', 'valence']
attributes = ['acousticness', 'popularity']
data = data[attributes]

#print(data.head(5))

#creat x and y plots
x = np.array(data.drop(['acousticness'], 1)) [:1000]
y = np.array(data.drop(['popularity'], 1)) [:1000]

#create linear regression model
model = LinearRegression()
model.fit(x, y)

x_new = np.linspace(0, 30, 100)
y_new = model.predict(x_new[:, np.newaxis])

#show data
# plot the results
valid =  data[x.shape[0]:]
plt.title('Model')
plt.xlabel('Acousticness',fontsize=18)
plt.ylabel('Popularity',fontsize=18)
plt.scatter(x,y)
plt.plot(x_new,y_new, 'k')

plt.show()


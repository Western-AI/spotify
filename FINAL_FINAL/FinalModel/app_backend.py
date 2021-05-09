from flask import Flask, redirect, url_for, render_template, request

from Main import *

att = ['acousticness', 'danceability', 'energy', 'explicit',
       'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
       'speechiness', 'tempo', 'valence', 'year']

dict = {}
userAtt = []
graph = ""

mainObj = Main()

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        for item in att:
            dict[item] = request.form[item]

        file = open('output.txt', 'w')
        for item in dict.keys():
            file.write(item + ":" + dict[item] + "\n")
            userAtt.append(int(dict[item]))
        file.close()

        graph = int(request.form["graphChoice"])

        predicted_value = mainObj.PredictValues(graph, userAtt)

        if graph == 0:
            print('Summing model with estime popularity of ', predicted_value)
        else:
            print('AllPoly model with estime popularity of ', predicted_value)

        print("*" * 20)
        print("Random Song Tester")
        main = mainObj.grabRealSong(graph)
        print('actual: ', main[0])
        print('predicted: ', main[1])
        print('\n')

        """
        print("\nALL MODELS:\n")
        print("summing model guess", main.PredictValues(0,inputdata))
        print("Poly model guess", main.PredictValues(1,inputdata))
        """
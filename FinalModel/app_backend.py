from flask import Flask, redirect, url_for, render_template, request

att = ['acousticness', 'danceability', 'energy', 'explicit',
       'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
       'speechiness', 'tempo', 'valence', 'year']

dict = {}
userAtt = []
graph = ""


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        for item in att:
            dict[item] = request.form[item]

        file = open('output.txt', 'w')
        for item in dict.keys():
            file.write(item + ":" + dict[item] + "\n")
            userAtt.append(dict[item])
        file.close()
        
        graph = request.form["graphChoice"]

        print(graph)
        print(dict)
        print(userAtt)
        return render_template("index.html", data = dict)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template
import workforce

app=Flask(__name__)

@app.route("/")
def root():
    return render_template("base.html")

@app.route("/occupations")
def occupations():
    dictionary = dic()
    return render_template("base.html",ranName=job(dictionary), data=dictionary)

def job(data):
    return workforce.randJob(-1, data)

def dic():
    file = open("occupations.csv", "r")
    data = workforce.parseCSV(file.read(), False)
    data = workforce.makeDictionary(data)
    file.close()
    return data

if __name__=="__main__":
    app.debug=True
    app.run()

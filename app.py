from flask import Flask, render_template
import workforce

app=Flask(__name__)

@app.route("/")
def root():
    return render_template("base.html")

@app.route("/occupations")
def occupations():
    file = open("occupations.csv", "r")
    content = file.read().replace("\n", "<br>")
    file.close()
    return content


if __name__=="__main__":
    app.debug=True
    app.run()

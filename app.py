from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def root():
    return render_template("base.html")

@app.route("/occupation")
def occupations():
   #return 


if __name__=="__main__":
    app.debug=True
    app.run()
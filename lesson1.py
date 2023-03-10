from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/souvenir")
def souvenir():
    return render_template("souvenir.html")

@app.route("/greeting")
def greeting():
    return render_template("greeting.html")

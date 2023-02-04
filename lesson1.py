from flask import Flask, render_template

app = Flask(__name__)

print("git")

@app.route("/")
def hello():
    return render_template("main.html")
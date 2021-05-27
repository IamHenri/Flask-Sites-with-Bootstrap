#Source : https://iq.opengenus.org/single-page-application-with-flask-ajax/
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

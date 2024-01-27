from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    """Index creates the site that's shown"""
    return render_template("index.html")

from click import open_file
from flask import Flask, redirect, url_for, render_template, jsonify, json, request
from hoc import runwithCache
import os


heading_links = {}

equitybullURL = "https://www.equitybulls.com/"
app = Flask(__name__)


heading_links = runwithCache(url=equitybullURL, cache_time=300)


@app.route("/")
def hello_world():
    return render_template("index.html", headings_links=heading_links)


@app.route("/news")
def news_dict():
    return render_template("index.html")


@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin"))


@app.route("/base", methods=['GET', 'POST'])
def base():
    if request.method == 'POST' or request.method == 'GET':
        formData = request.form.get('query')
        
        # make ML call here
    
        
        print("formData -->", formData)
    return render_template("base.html", heading_links=heading_links)


# run if unknown route
@app.route("/<name>")
def user(name):
    return f"Hello {name}"


if __name__ == "__main__":
    if (heading_links == -1):
        print('equitybulls website is down')
        print("app stopped")
    else:
        print('equitybulls website is running')
        print('app starting ...')
        app.run(debug=True, port=5000)

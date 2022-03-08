from flask import Flask, redirect, url_for, render_template, jsonify, json
from EquityBulls import headings_links

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", headings_links=headings_links)


@app.route("/news")
def news_dict():
    return render_template("index.html")


@app.route("/<name>")
def user(name):
    return f"Hello {name}"


@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin"))


if __name__ == "__main__":
    app.run(debug=True)
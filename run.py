import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3])


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "127.0.0.1"),
        port=int(os.environ.get("PORT", "8080")),
        debug=True
    )
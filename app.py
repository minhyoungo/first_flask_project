from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/1")
def page1():
    return render_template("page2.html", login_name="OMH")


@app.route("/2")
def page2():
    return render_template("page1.html")


if __name__ == '__main__':
    app.run(debug=True)

# <iframe width = "900" height = "506" src = "https://www.youtube.com/embed/MRY26k7sUkY" title = "YouTube video player" frameborder = "0" allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen > </iframe >

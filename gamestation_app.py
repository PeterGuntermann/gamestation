from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("main_page.html", user="Fremder")


@app.route("/foobar", methods=("GET",))
def getFoobar():
    return "foo"


@app.route("/foobar", methods=("POST",))
def postFoobar():
    return "bar"


if __name__ == '__main__':
    app.run(debug=True)

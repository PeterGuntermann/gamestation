from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main_page.html", user="Fremder")


if __name__ == '__main__':
    app.run(debug=True)
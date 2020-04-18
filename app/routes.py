from flask import render_template, request, Response
from app import app

users = []


@app.route("/")
@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/lobby")
def lobby():
    return render_template("lobby.html", users=users)


@app.route("/set-username", methods=("POST",))
def set_username():
    payload = request.json
    if payload is not None:
        users.append(payload["username"])
        return Response(status=200)

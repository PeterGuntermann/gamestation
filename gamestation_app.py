from flask import Flask, render_template, request, Response

app = Flask(__name__)

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
        # user.set_name(payload["username"])
        users.append(payload["username"])
        return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True)

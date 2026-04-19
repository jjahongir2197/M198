from flask import Flask, render_template, request

app = Flask(__name__)

users = []

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users.append({"username": username, "password": password})

        return render_template("result46.html", users=users)

    return render_template("index46.html")

if __name__ == "__main__":
    app.run(debug=True)

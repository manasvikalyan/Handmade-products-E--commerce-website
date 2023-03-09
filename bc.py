from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Create a list of users for authentication
users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "user3", "password": "password3"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        for user in users:
            if user["username"] == username and user["password"] == password:
                return redirect("/dashboard")

        # If the username or password is incorrect, show an error message
        error = "Invalid credentials. Please try again."
        return render_template("login.html", error=error)

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return "Welcome to the dashboard!"

if __name__ == "__main__":
    app.run(debug=True)

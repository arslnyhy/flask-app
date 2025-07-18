from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/profile")
def profile():
    return render_template("profile.html", name="Arsalan")


@app.route("/users")
def users():
    users_list = ["Arsalan", "Farshind", "Ali"]
    return render_template("users.html", users=users_list)


@app.route("/check")
def check_login():
    return render_template("check.html", is_logged_in=False, name="Arsalan")


@app.route("/about")
def about():
    return "This is the about page."


@app.route("/course/<string:course_name>")
def show_course(course_name):
    return f"Page for the {course_name} course"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Logging in..."
    return "Login form"


if __name__ == "__main__":
    app.run(debug=True)

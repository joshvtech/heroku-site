from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("pages/index.html")

@main.route("/about")
def about():
    return render_template("pages/about.html")

@main.route("/contact")
def contact():
    return render_template("pages/contact.html")

@main.route("/contact", methods=["POST"])
def contact_post():
    pass
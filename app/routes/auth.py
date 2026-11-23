from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/")
def index():
    return render_template("index.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("All fields are required")
            return render_template("register.html")

        service = current_app.extensions["user_service"]
        try:
            service.register(name, email, password)
        except ValueError as error:
            flash(str(error))
            return render_template("register.html")

        flash("Registration successful")
        return redirect(url_for("auth.index"))

    return render_template("register.html")

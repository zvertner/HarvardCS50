import os

# Import necessary modules from the cs50 library
from cs50 import SQL
# Import necessary modules from Flask for web application
from flask import Flask, flash, redirect, render_template, request, session
# Import Session module from Flask-Session for session management
from flask_session import Session
# Import mkdtemp to create a temporary directory for session files
from tempfile import mkdtemp
# Import security functions for password hashing and verification
from werkzeug.security import check_password_hash, generate_password_hash
# Import helper functions from the local helpers.py file
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///user.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show Homepage"""
    return render_template("index.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id from the session
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to homepage
        return redirect("/")

    # User reached route via GET rendering login form (by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id from the session
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/howto", methods=["GET", "POST"])
@login_required
def howto():
    """Go to HowTo."""
    # Render the howto.html template
    if request.method == "GET":
        return render_template("howto.html")

@app.route("/references", methods=["GET", "POST"])
@login_required
def references():
    # Render the references.html template
    """References."""
    if request.method == "GET":
        return render_template("references.html")


@app.route("/contact", methods=["GET", "POST"])
@login_required
def contact():
    # Render the contacts.html template
    """contacts page."""
    if request.method == "GET":
        return render_template("contact.html")


@app.route("/challenge", methods=["GET", "POST"])
@login_required
def challenge():
    # Render the challenge.html template (sample answers to fillin the blank quiz questions)
    """Editing challenge."""
    if request.method == "GET":
        return render_template("challenge.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Handle GET request (render registration form)
    if request.method == "GET":
        return render_template("register.html")
    # Handle POST request (form submission)
    else:
     # Retrieve form inputs
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
    # Validate form inputs
        if not username:
            return apology("Please provide username.")
        elif not password:
            return apology("Please provide password.")
        elif not confirmation:
            return apology("Please confirm password.")
        if password != confirmation:
            return apology("Please make sure passwords match.")
        # Hash the user's password
        hash = generate_password_hash(password)
        # Attempt to register new user in the database
        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
        except:
            return apology("Username previously registered.")
        # Log the new user in by setting session user_id
        session["user_id"] = new_user
        # Redirect user to home page
        return redirect("/")

@app.route("/quiz", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Render the quiz.html template
    if request.method == "GET":
        return render_template("quiz.html")

# Module to interact with the operating system
import os
# Module to make HTTP requests
import requests
# Module for parsing URLs
import urllib.parse

from flask import redirect, render_template, request, session  # Import specific functions from Flask
from functools import wraps  # Import wraps to create decorator functions


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if user is logged in
        if session.get("user_id") is None:
        # Redirect to login page if not logged in
            return redirect("/login")
        # Proceed with the original function if logged in
        return f(*args, **kwargs)
    return decorated_function

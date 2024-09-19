import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from datetime import datetime, timedelta
import time


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdate.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    session.clear()
    # Delete last birthdate from SQL database
    db.execute("DELETE FROM birthdates")

    if request.method == "POST":
        # Ensure birthdate was picked
        if not request.form.get("birthday"):
            flash("Must pick birthdate")
        else:
            # Get the date from the user
            birthday = request.form.get("birthday")
            session["birthday"] = birthday

            # Storing the dates in variable for the calculation
            start = datetime.strptime(birthday, "%Y-%m-%d")
            today = time.strftime("%Y-%m-%d")
            end = datetime.strptime(today, "%Y-%m-%d")

            # Storing user's birthdate in SQL database
            db.execute("INSERT INTO birthdates (date) VALUES (?)", start)

            # Getting the difference between the years
            difference = end - start
            seconds = difference.total_seconds()
            age = int(seconds / (60 * 60 * 8760))

            return render_template("index.html", age=age)

    return render_template("index.html")


@app.route("/duration", methods=["GET", "POST"])
def duration():
    session.clear()

    if request.method == "POST":
        # Ensure start date was picked
        if not request.form.get("start"):
            flash("Must pick start date")

        # Ensure end date was picked
        elif not request.form.get("end"):
            flash("Must pick end date")

        else:
            # Get the date from the user
            session["start"] = request.form.get("start")
            session["end"] = request.form.get("end")

            # Storing the dates in variable for the calculation
            start = datetime.strptime(session["start"], "%Y-%m-%d")
            end = datetime.strptime(session["end"], "%Y-%m-%d")

            # Getting the difference between the years
            difference = end - start

            # Algorithm to get the difference precisely FROM years to days
            difference = difference.days
            years = 0
            months = 0
            weeks = 0
            days = 0

            # Count years
            while difference >= 365:
                difference = difference - 365
                years += 1
                session[
                    "duration"
                ] = 1  # Check if anything is counted to render in HTML
            # Count months
            while difference >= 30:
                difference = difference - 30
                months += 1
                session["duration"] = 1
            # Count weeks
            while difference >= 7:
                difference = difference - 7
                weeks += 1
                session["duration"] = 1
            # Count days
            while difference >= 1:
                difference = difference - 1
                days += 1
                session["duration"] = 1

            return render_template(
                "duration.html", years=years, months=months, weeks=weeks, days=days
            )
    return render_template("duration.html")


@app.route("/tracker")
def tracker():
    # Find birthdate and track the date by SQL
    check = db.execute("SELECT COUNT(*) FROM birthdates")

    if check[0]["COUNT(*)"] == 0:
        # Clear last tracker and tell the user to pick the birthdate
        session.clear()
        flash("Must pick birthdate")
        return render_template("tracker.html")

    else:
        # Fetch the birthdate
        birthdate = db.execute("SELECT date FROM birthdates")
        birthdate = birthdate[0]["date"]

        # Extract the day and month only in specific format
        edit = birthdate[:10]
        day_month = edit[5:]
        date = day_month.replace("-", "/") + "/"

        # Delete last birthdate from SQL database
        db.execute("DELETE FROM birthdates")

        # Remeber the last day and month
        session["day_month"] = date
        print(date)
        return render_template("tracker.html", date=date)

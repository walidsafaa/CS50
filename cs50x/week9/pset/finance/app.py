import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    cash_user = db.execute("SELECT cash FROM users WHERE id == ?", session["user_id"])
    cash = usd(cash_user[0]["cash"])
    data = db.execute(
        "SELECT SUM(amount) as amount FROM log WHERE user_id == ? AND shares > 0",
        session["user_id"],
    )
    amount = data[0]["amount"]
    data = db.execute(
        "SELECT SUM(shares) as shares FROM log WHERE user_id == ?", session["user_id"]
    )

    check = db.execute(
        "SELECT COUNT(*) FROM log WHERE user_id == ?",
        session["user_id"],
    )
    if check[0]["COUNT(*)"] == 0:
        amount = 0
        total = usd(cash_user[0]["cash"] + amount)
        results = db.execute("SELECT * FROM mix WHERE user_id = ?", session["user_id"])
        return render_template("index.html", cash=cash, total=total, results=results)
    total = usd(cash_user[0]["cash"] + amount)
    results = db.execute("SELECT * FROM mix WHERE user_id = ?", session["user_id"])
    return render_template("index.html", cash=cash, total=total, results=results)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        # get the cash of the user
        cash_user = db.execute(
            "SELECT cash FROM users WHERE id == ?", session["user_id"]
        )  ##Fixed
        cash = cash_user[0]["cash"]
        if not request.form.get("shares"):
            return apology("Not a number", 400)
        else:
            shares = request.form.get("shares")
            if lookup(symbol) != None:
                results = lookup(symbol)

                # check if the user can afford it or not
                if cash >= (results["price"] * float(shares)):
                    # update current cash
                    amount = results["price"] * float(shares)
                    current_cash = cash - amount
                    db.execute(
                        "UPDATE users SET cash = ? WHERE id == ?",
                        current_cash,
                        session["user_id"],
                    )
                    # check first time for stock
                    check = db.execute("SELECT COUNT(*) FROM stocks")
                    check_symbol = db.execute(
                        "SELECT symbol FROM stocks WHERE symbol == ?", symbol
                    )

                    if check[0]["COUNT(*)"] == 0:
                        # First stock
                        db.execute(
                            "INSERT INTO stocks (id, symbol, price) VALUES(?, ?, ?)",
                            1,
                            symbol,
                            results["price"],
                        )
                    else:
                        last = db.execute(
                            "SELECT id FROM stocks ORDER BY id DESC LIMIT(1)"
                        )

                        if check_symbol == []:  # CHECK IF THERE NO SYMBOL LIKE THIS
                            print("3")
                            db.execute(
                                "INSERT INTO stocks (id, symbol, price) VALUES(?, ?, ?)",
                                last[0]["id"] + 1,
                                symbol,
                                results["price"],
                            )

                    # Log
                    last_2 = db.execute(
                        "SELECT id FROM stocks WHERE symbol == ? ORDER BY id DESC LIMIT(1)",
                        symbol,
                    )
                    # Remember which symbol has been bought
                    session["symbol_id"] = last_2[0]["id"]
                    # time
                    dt = datetime.now()
                    x = dt.replace(microsecond=0)
                    # Store log in DB
                    db.execute(
                        "INSERT INTO log (user_id, symbol_id, symbol, price, shares, amount, datetime) VALUES(?, ?, ?, ?, ?, ?, ?)",
                        session["user_id"],
                        session["symbol_id"],
                        symbol,
                        results["price"],
                        shares,
                        amount,
                        x,
                    )
                    # check if stock exists
                    stocks = db.execute(
                        "SELECT stocks.id, stocks.symbol, stocks.price, SUM(log.shares) as shares, SUM(log.amount) as total FROM users JOIN log ON users.id = log.user_id JOIN stocks ON log.symbol_id = stocks.id WHERE log.user_id = ? AND log.symbol_id = ?",
                        session["user_id"],
                        session["symbol_id"],
                    )
                    # check if it already exist before
                    check = db.execute(
                        "SELECT COUNT(*) FROM mix WHERE user_id == ? AND symbol_id == ?",
                        session["user_id"],
                        session["symbol_id"],
                    )
                    if check[0]["COUNT(*)"] == 0:
                        for row in stocks:
                            id = row["id"]
                            symbol = row["symbol"]
                            price = row["price"]
                            shares = row["shares"]
                            total = row["total"]
                            if row["shares"] > 0:
                                db.execute(
                                    "INSERT INTO mix (user_id, symbol_id, symbol, price, shares, total) VALUES (?, ?, ?, ?, ?, ?)",
                                    session["user_id"],
                                    id,
                                    symbol,
                                    usd(price),
                                    shares,
                                    usd(total),
                                )

                    else:
                        for row in stocks:
                            id = row["id"]
                            symbol = row["symbol"]
                            price = row["price"]
                            shares = row["shares"]
                            total = row["total"]
                            if row["shares"] > 0:
                                db.execute(
                                    "UPDATE mix SET user_id = ?, symbol_id = ?, symbol = ?, price = ?, shares = ?, total = ? WHERE symbol_id == ?",
                                    session["user_id"],
                                    id,
                                    symbol,
                                    usd(price),
                                    shares,
                                    usd(total),
                                    session["symbol_id"],
                                )
                            else:
                                db.execute(
                                    "DELETE FROM mix WHERE user_id == ? AND symbol_id == ?",
                                    session["user_id"],
                                    id,
                                )

                    return redirect("/")
                else:
                    return apology("No enough cash", 400)

        return apology("Inputs are not valid", 400)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    log = db.execute("SELECT * FROM log WHERE user_id == ?", session["user_id"])
    stocks = db.execute(
        "SELECT id, symbol, price from stocks WHERE id IN (SELECT symbol_id FROM log WHERE user_id == ?)",
        session["user_id"],
    )

    check = db.execute(
        "SELECT COUNT(*) FROM log WHERE user_id == ?", session["user_id"]
    )

    if check[0]["COUNT(*)"] == 0:
        text = "No Transactions"
        return render_template("history.html", text=text)
    else:
        return render_template("history.html", log=log, stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
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
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["login"] = 1

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if lookup(symbol) != None:
            results = lookup(symbol.upper())
            return render_template(
                "quoted.html",
                name=results["name"],
                symbol=results["symbol"],
                price=usd(results["price"]),
            )

        return apology("Symbol is not found", 400)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # storing current usernames in list
        usernames = []
        usernames_db = db.execute("SELECT username FROM users;")
        for row in usernames_db:
            name = row["username"]
            usernames.append(name)

        if not username:
            return apology("No username!", 400)
        elif not password:
            return apology("No password!", 400)
        elif not confirmation:
            return apology("No confirmation!", 400)
        elif password != confirmation:
            return apology("Doesn't match", 400)
        elif username in usernames:
            return apology("Username already exists", 400)
        else:
            hash = generate_password_hash(password)
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash
            )
            # Redirect user to home page
            return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    stocks = db.execute(
        "SELECT * FROM mix WHERE symbol_id IN (SELECT DISTINCT(symbol_id) FROM log WHERE user_id == ?)",
        session["user_id"],
    )
    cash_user = db.execute("SELECT cash FROM users WHERE id == ?", session["user_id"])
    cash = cash_user[0]["cash"]
    if request.method == "POST":
        stock = request.form.get("symbol").upper()
        number = int(request.form.get("shares"))
        max = db.execute(
            "SELECT SUM(shares) as shares, price FROM log WHERE symbol == ?", stock
        )
        id = db.execute("SELECT id FROM stocks WHERE symbol == ?", stock)
        if not stock or number > max[0]["shares"]:
            return apology("Inputs are not valid.")  # In case any error
        else:
            amount = float(number) * float(max[0]["price"])
            sold = -(number)
            # UPDATE CURRENT CASH
            current_cash = cash + amount
            db.execute(
                "UPDATE users SET cash = ? WHERE id == ?",
                current_cash,
                session["user_id"],
            )
            # Remember which symbol has been bought
            session["symbol_id"] = id[0]["id"]
            # time
            dt = datetime.now()
            x = dt.replace(microsecond=0)
            # Store log in DB
            db.execute(
                "INSERT INTO log (user_id, symbol_id, symbol, price, shares, amount, datetime) VALUES(?, ?, ?, ?, ?, ?, ?)",
                session["user_id"],
                session["symbol_id"],
                stock,
                max[0]["price"],
                sold,
                -(amount),
                x,
            )
            # check if stock exists
            stocks = db.execute(
                "SELECT stocks.id, stocks.symbol, stocks.price, SUM(log.shares) as shares, SUM(log.amount) as total FROM users JOIN log ON users.id = log.user_id JOIN stocks ON log.symbol_id = stocks.id WHERE log.user_id = ? AND log.symbol_id = ?",
                session["user_id"],
                session["symbol_id"],
            )
            # check if it already exist before
            check = db.execute(
                "SELECT COUNT(*) FROM mix WHERE user_id == ? AND symbol_id == ?",
                session["user_id"],
                session["symbol_id"],
            )
            if check[0]["COUNT(*)"] == 0:
                for row in stocks:
                    id = row["id"]
                    symbol = row["symbol"]
                    price = row["price"]
                    shares = row["shares"]
                    total = row["total"]
                    if row["shares"] > 0:
                        db.execute(
                            "INSERT INTO mix (user_id, symbol_id, symbol, price, shares, total) VALUES (?, ?, ?, ?, ?, ?)",
                            session["user_id"],
                            id,
                            symbol,
                            usd(price),
                            shares,
                            usd(total),
                        )

            else:
                for row in stocks:
                    id = row["id"]
                    symbol = row["symbol"]
                    price = row["price"]
                    shares = row["shares"]
                    total = row["total"]
                    if row["shares"] > 0:
                        db.execute(
                            "UPDATE mix SET user_id = ?, symbol_id = ?, symbol = ?, price = ?, shares = ?, total = ? WHERE symbol_id == ?",
                            session["user_id"],
                            id,
                            symbol,
                            usd(price),
                            shares,
                            usd(total),
                            session["symbol_id"],
                        )
                    else:
                        db.execute(
                            "DELETE FROM mix WHERE user_id == ? AND symbol_id == ?",
                            session["user_id"],
                            id,
                        )
            # Redirect user to home page
            return redirect("/")
    else:
        return render_template("sell.html", stocks=stocks)

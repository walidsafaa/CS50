from cs50 import SQL

db = SQL("sqlite:///finance.db")

stocks = db.execute("SELECT stocks.id, stocks.symbol, stocks.price, SUM(log.shares) as shares, SUM(log.amount) as total FROM users JOIN log ON users.id = log.user_id JOIN stocks ON log.symbol_id = stocks.id WHERE log.user_id = 1 AND log.symbol_id = 1")

#check if it already exist before
check = db.execute("SELECT COUNT(*) FROM mix WHERE symbol_id == 1")
if check[0]['COUNT(*)'] == 0:
    for row in stocks:
        id = row['id']
        symbol = row['symbol']
        price = row['price']
        shares = row['shares']
        total = row['total']
    db.execute("INSERT INTO mix (symbol_id, symbol, price, shares, total) VALUES (?, ?, ?, ?, ?)", id, symbol, price, shares, total)
else:
    for row in stocks:
        id = row['id']
        symbol = row['symbol']
        price = row['price']
        shares = row['shares']
        total = row['total']
    db.execute("UPDATE mix SET symbol_id = ?, symbol = ?, price = ?, shares = ?, total = ? WHERE symbol_id == 1", id, symbol, price, shares, total)

results = db.execute("SELECT * FROM mix")
print(results)


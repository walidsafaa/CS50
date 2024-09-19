from cs50 import SQL

db = SQL("sqlite:///test.db")

favourite = input("Favourite: ")

rows = db.execute("SELECT COUNT(*) as n FROM test where TATC = ?", favourite)

print(rows[0]["n"])
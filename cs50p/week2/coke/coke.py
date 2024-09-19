total = 50
while total > 0:
    print(f"Amount Due: {total}")
    x = int(input("Insert Coin: "))
    if x == 25:
        total = total - 25
    elif x == 10:
        total = total - 10
    elif x == 5:
        total = total - 5

print(f"Change Owed: {abs(total)}")

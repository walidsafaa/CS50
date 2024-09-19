list = {}
while True:
    try:
        item = input().strip().upper()
        if item not in list:
            list[item] = 1
        else:
            list[item] += 1
    except EOFError:
        for row in sorted(list):
            print(list[row], row, sep=" ")
        break
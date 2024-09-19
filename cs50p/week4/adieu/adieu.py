names = []
while True:
    try:
        name = input("Name: ").title()
        names.append(name)
    except EOFError:
        break

print("Adieu, adieu, to ", end="")
count = 1
for name in names:
    if len(names) == 1:
        print(name)
    elif len(names) == 2 and count == 1:
        print(name, end=" ")
    elif len(names) == 2 and count == 2:
        print("and", name)
    elif len(names) > 2 and count == len(names):
        print("and", name)
    else:
        print(name, end=", ")
    count += 1

def main():
    camelCase = input("camelCase: ")
    snake_case(camelCase)


def snake_case(camel):
    for c in camel:
        if c.isupper():
            camel = camel.replace(c, "_" + c.lower())
    print("snake_case: " + camel)


main()

'''
camel = input("camelCase: ")
print("snake_case: ", end="")

for c in camel:
    if c.islower():
        print(c, end="")
    if c.isupper():
        print("_", c.lower(), end="", sep="")

print()
'''
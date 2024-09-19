import re

greeting = input("Greeting: ")

if "hello" in greeting.lower():
    print("$0")
elif re.search("^h", greeting, re.IGNORECASE):
    print("$20")
else:
    print("$100")
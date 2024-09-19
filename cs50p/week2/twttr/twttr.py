text = input("Input: ")
vowels = ["A", "E", "I", "O", "U"]

for c in text:
    if c.upper() in vowels:
        text = text.replace(c, "")

print(f"Output: {text}")

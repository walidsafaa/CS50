text = input("Enter text: ").replace(":)", "🙂").replace(":(","🙁")

print(text)
'''
def main():
    text = input("Enter text: ")
    convert(text)


def convert(text):
    count = 0
    dict = text.split()
    for i in dict:
        if i == ':)':
            print('🙂 ', end="")
        elif i == ':(':
            print('🙁 ', end="")
        else:
            print(f"{i} ", end="")
        if count == len(dict) - 1:
            print()
        count+=1

main()
'''
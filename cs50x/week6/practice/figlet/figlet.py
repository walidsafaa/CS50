import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            s = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(s))
            sys.exit(0)
        else:
            print("Invalid usage")
            sys.exit(1)
elif len(sys.argv) == 1:
    s = input("Input: ")
    print(figlet.renderText(s))
    sys.exit(0)
else:
    print("Invalid usage")
    sys.exit(1)

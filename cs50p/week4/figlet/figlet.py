from pyfiglet import Figlet
import sys
import random

# Check the command lines
if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid usage")

if len(sys.argv) == 3 and sys.argv[1] not in ["-f", "--font"]:
    sys.exit("Invalid usage")

# Rename the module in a variable
figlet = Figlet()

# Check if the font is random or not
if len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
else:
    figlet.setFont(font=random.choice(figlet.getFonts()))

# Prompt the user for a text
text = input()

# Print the text in a specific font
print(figlet.renderText(text))

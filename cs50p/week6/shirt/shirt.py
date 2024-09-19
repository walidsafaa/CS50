import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-4:].lower() != ".jpg" and sys.argv[1][-4:].lower() != ".png" and sys.argv[1][-5:].lower() != ".jpeg":
            sys.exit("Invalid input")
    elif sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower() and sys.argv[1][-5:].lower() != sys.argv[2][-5:].lower():
        sys.exit("Input and output have different extensions")
    else:
        convert(sys.argv[1], sys.argv[2])

def convert(input, output):
    try:
        #shirt
        shirt = Image.open("shirt.png")
        # Get size of shirt photo
        size = shirt.size
        # open input
        with Image.open(input) as input:
            input = ImageOps.fit(input, size)
            #Overlay the shirt on the input in specific size
            input.paste(shirt, mask= shirt)
            #Save new updated input into output's name
            input.save(output)

    except FileNotFoundError:
        raise FileNotFoundError


if __name__ == "__main__":
    main()
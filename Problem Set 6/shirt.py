import sys
from PIL import Image

try:
    if len(sys.argv) < 3:
        sys.exit("Too few arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too much arguments.")

    if not sys.argv[1].endswith(".jpg") and not sys.argv[1].endswith(".jpeg") and not sys.argv[1].endswith(".png"):
        sys.exit("Invalid input") 
    elif not sys.argv[2].endswith(".jpg") and not sys.argv[2].endswith(".jpeg") and not sys.argv[2].endswith(".png"):
        sys.exit("Invalid input")

    if len(sys.argv) == 3:
        shirt = Image.open("shirt.png")
        mine = Image.open(sys.argv[1])
        size = mine.size
        s = shirt.size
        mine = mine.resize(s)
        mine.paste(shirt, (0, 0), shirt)
        mine.save(sys.argv[2])
        
except FileNotFoundError:
    sys.exit("File not found.")
import random
import string

# Create a new key
def generate():
    letters=list(string.ascii_lowercase)
    random.shuffle(letters)
    print(letters)


generate()



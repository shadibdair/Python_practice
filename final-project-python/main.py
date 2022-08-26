import random
import string

# Create a new key
def generate():
    letters=string.ascii_lowercase
    print(letters)
    random.shuffle(letters)
    print(letters)

generate()


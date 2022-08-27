# Imports
import random
import string

def new_enc_key():
    encryption = list(string.ascii_lowercase)
    #print("enc: ", encryption)

    letters_list = list(encryption)
    shuffled = random.shuffle(letters_list)
    #decryption = ''.join(encryption)
    #print("dec: ", letters_list)
    # This is the Key that I need to encrypt the words
    key = {encryption[i]:letters_list[i] for i in range(len(encryption))}
    #print(f"A new key called {name} was created")
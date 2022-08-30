import random
import string


def defencdec():
    encryption = list(string.ascii_lowercase)
    #print("enc: ", encryption)
    letters_list = list(encryption)
    shuffled = random.shuffle(letters_list)
    #decryption = ''.join(encryption)
    # This is the Key that I need to encrypt the words
    key = {encryption[i]:letters_list[i] for i in range(len(encryption))}
    decryption = {value: key for key, value in key.items()}
    return key, decryption
    #print(f"A new key called {name} was created")

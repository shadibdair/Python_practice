# Imports
import random
import string

def new_enc_key():
    encryption = list(string.ascii_lowercase)
    print("enc: ", encryption)
    random.shuffle(encryption)
    #decryption = encryption
    decryption = ''.join(encryption)
    print("dec: ", decryption)
    print("\n \n")
    key = {encryption[i]:decryption[i] for i in range(len(encryption))}
    print(key)
    print("A new key called {} was created")
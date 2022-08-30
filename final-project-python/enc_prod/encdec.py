# Function that decrypt the text dec
def encryption_decryption(dec_file, enc, dec):
    enc = ''
    with open(dec_file, "r") as file:
        str = file.read()
        list = list(str)
        for letter in list:
            if letter in dec_file:
                enc += dec_file[letter]
            else:
                enc += letter
    with open(dec, "w") as dec_file:
        dec_file.write(enc)
    return 0


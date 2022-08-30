# Imports && From
from encjsonconvert import from_json, to_json
import string
from enckey import defencdec as dec_enc_
from encdec import encryption_decryption
# --------------------------------------------


# Function that created key
def enckey_(newkey):
    key, encdec_ = dec_enc_()
    # Output with the name of the file that was choosen from the user.
    print(f"A new key called {newkey} was created")
    return key, encdec_

# Function encdec_ the text 
def encdec_(enc_file, dec_file, encdec_):
    value = encryption_decryption(encdec_, enc_file, dec_file)
    if value == 1:
        return value
    # Output with the name of the file that was decrypted.
    print(f"File {enc_file} was decrypted into {dec_file}")
    return value

# Function that saves the file key 
def encsave_(file, key, encdec_, nameKey):
    value = to_json(key, encdec_, file, nameKey)
    if value == 1:
        return value
    print(f"Enc/encdec_ keys saved in {file} file")
    return value

# Function that load the file 
def encload_(file):
    key, encdec_, nameKey = from_json(file)
    if key:
        print(f"Key {nameKey} from file {file} loaded")
    return key, encdec_, nameKey

def encinfo_(nameKey, key, encdec_, save, *more):
    letters = string.ascii_lowercase
    print("Current key:", nameKey)
    if save:
        print("state:", "saved in", more[0])
    else:
        print("state: not saved")
    print("enc:\t\t", letters)
    print("\t", ''.join([value for key, value in key.items()]))
    print("encdec_:")
    print("\t", ''.join([key for key, value in encdec_.items()]))
    print(letters)

# Function enc the text
def enc(enc_file, dec_file, key):
    value = encryption_decryption(key, enc_file, dec_file)
    if value == 1:
        return value
    print(f"File {enc_file} was encrypted into {dec_file}")
    return value

# The Commands that program can run.
commands = {
    'newkey': enckey_, 'info': encinfo_, 'enc': enc,'load': encload_, 'encdec_': encdec_, 'save': encsave_
}

# The main function that run CLI command.
def cli():
    # -------------
    cli_end = False
    save = False
    exist = False
    nameKey = ''
    nameFile = ''
    key = dict()
    encdec_ = dict()
    # -------------

    while not cli_end:
        cmd_str = input('subs>')
        cmd = cmd_str.split()
        if not cmd:
            continue
        if cmd[0] == 'done':
            cli_end = True
            continue
        if cmd[0] not in commands:
            print("Command not Found")
            continue
        if exist and cmd[0] == "info":
            if not nameFile:
                save = False
            else:
                check1, check2, check3 = from_json(
                    nameFile, "No Print")
                if not check1 or not check2 or not check3:
                    save = False
                    nameFile = ''
            commands[cmd[0]](nameKey, key, encdec_, save, nameFile)
            continue
        if len(cmd) < 2:
            continue
        if cmd[0] == "newkey":
            key, encdec_ = commands[cmd[0]](cmd[1])
            nameKey = cmd[1]
            exist = True
            save = False
            nameFile = ''
            continue
        if cmd[0] == "load":
            k_tmp, dec_tmp, key_tmp = commands[cmd[0]](
                cmd[1])
            if not dec_tmp or not k_tmp or not key_tmp:
                continue
            key, encdec_, nameKey = k_tmp, dec_tmp, key_tmp
            exist = True
            save = True
            nameFile = cmd[1]
            continue
        if not exist:
            print("There's no key !")
            continue
        if cmd[0] == "save":
            commands[cmd[0]](cmd[1], key, encdec_, nameKey)
            save = True
            nameFile = cmd[1]
            continue
        if (len(cmd) < 3):
            continue
        if cmd[0] == "enc":
            commands[cmd[0]](cmd[1], cmd[2], key)
            continue
        if cmd[0] == "encdec_":
            commands[cmd[0]](cmd[1], cmd[2], encdec_)
            continue
# Call the main function
cli()

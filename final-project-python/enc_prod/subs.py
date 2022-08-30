# Imports && From
from encjsonconvert import from_json, to_json
from enckey import defencdec as dec_enc_
import string
from encdec import encjsonconvert
# --------------------------------------------


# Function that created key
def _enckey_(my_key):
    dic_enc, dic_dec = dec_enc_()
    # Output with the name of the file that was choosen from the user.
    print(f"A new key called {my_key} was created")
    return dic_enc, dic_dec

# Function that saves the file key 
def _encsave_(file, dic_enc, dic_dec, nameKey):
    ret = to_json(dic_enc, dic_dec, file, nameKey)
    if ret == 1:
        return ret
    print(f"Enc/Dec keys saved in {file} file")
    return ret

def _encinfo_(nameKey, dic_enc, dic_dec, exist, *more):
    letters = string.ascii_lowercase

    print("Current key:", nameKey)
    if exist:
        print("state:", "saved in", more[0])
    else:
        print("state: not saved")
    print("_enc_:")
    print("\t", letters)
    print("\t", ''.join([value for key, value in dic_enc.items()]))
    print("_dec_:")
    print("\t", ''.join([key for key, value in dic_dec.items()]))
    print("\t", letters)

# Function that load the file 
def _encload_(file):
    dic_enc, dic_dec, nameKey = from_json(file)
    if dic_enc:
        print(f"Key {nameKey} from file {file} loaded")
    return dic_enc, dic_dec, nameKey

# Function enc the text
def _enc_(_from, _to, dic_enc):
    ret = encjsonconvert(dic_enc, _from, _to)
    if ret == 1:
        return ret
    print(f"File {_from} was encrypted into {_to}")
    return ret

# Function _dec_ the text
def _dec_(_from, _to, dic_dec):
    ret = encjsonconvert(dic_dec, _from, _to)
    if ret == 1:
        return ret
    print(f"File {_from} was decrypted into {_to}")
    return ret


# The main function that run CLI command.
commands = {
    'load': _encload_, 'newkey': _enckey_, 'info': _encinfo_, 'save': _encsave_, 'enc': _enc_, 'dec': _dec_
}

# The main function that run CLI command.
def cli():
    # --------------
    exist = False
    cli_end = False
    ExictKey = False
    nameKey = ''
    nameFile = ''
    dic_enc = dict()
    dic_dec = dict()
    # --------------

    while not cli_end:
        cmd_str = input('subs>')
        cmd = cmd_str.split()
        if not cmd:
            continue
        if cmd[0] == 'done':
            cli_end = True
            continue
        if cmd[0] not in commands:
            print("commands not Found")
            continue
        if ExictKey and cmd[0] == "info":
            if not nameFile:
                exist = False
            else:
                check1, check2, check3 = from_json(
                    nameFile, "No Print")
                if not check1 or not check2 or not check3:
                    exist = False
                    nameFile = ''
            commands[cmd[0]](nameKey, dic_enc, dic_dec, exist, nameFile)
            continue
        if len(cmd) < 2:
            continue
        if cmd[0] == "newkey":
            dic_enc, dic_dec = commands[cmd[0]](cmd[1])
            nameKey = cmd[1]
            ExictKey = True
            exist = False
            nameFile = ''
            continue
        if cmd[0] == "load":
            dic_enc_tmp, dic_dec_tmp, nameKey_tmp = commands[cmd[0]](
                cmd[1])
            if not dic_dec_tmp or not dic_enc_tmp or not nameKey_tmp:
                continue
            dic_enc, dic_dec, nameKey = dic_enc_tmp, dic_dec_tmp, nameKey_tmp
            ExictKey = True
            exist = True
            nameFile = cmd[1]
            continue
        if not ExictKey:
            print("There's no key!")
            continue
        if cmd[0] == "save":
            commands[cmd[0]](cmd[1], dic_enc, dic_dec, nameKey)
            exist = True
            nameFile = cmd[1]
            continue
        if (len(cmd) < 3):
            continue
        if cmd[0] == "enc":
            commands[cmd[0]](cmd[1], cmd[2], dic_enc)
            continue
        if cmd[0] == "dec":
            commands[cmd[0]](cmd[1], cmd[2], dic_dec)
            continue

# Call the main function
cli()

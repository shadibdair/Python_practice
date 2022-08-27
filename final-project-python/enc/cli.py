# Imports
import random
import string
#--------

# CLI program
def enc_init():
    commands = {
        'info': enc_info, 
        'load':enc_load, 
        'newkey':enc_key, 
        'save':enc_save
        }
    return commands


def main_cli():
    commands = enc_init()
    cli_end = False
    # While cli_end not False
    while not cli_end:
        # Output subs> everytime
        cmd_str = input('subs>')
        cmd = cmd_str.split()
        # Check If cmd not empty and in place [0] have word 'done' 
        if cmd and cmd[0] == 'done':
            cli_end = True
        if cmd:
            commands[cmd[0]](cmd[1:])
# ------------

def enc_save(self):
    print('_____save')

def enc_load(self):
    print('_____load')

def enc_key(self):
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

def enc_info(self):
    print('____info')

main_cli()
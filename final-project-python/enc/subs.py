# Imports
import random
import string
import enckey
import encload
import encsave
import encinfo
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
# Function save the Key inside File
def enc_save(self):
    save_key = encsave.save_key()
    print(save_key)
# Function that get the Key inside the File to use it for Enc/Dec
def enc_load(self):
    load_key = encload.load_key()
    print(load_key)
# Function that create the key
def enc_key(self):
    the_new_key = enckey.new_enc_key()
    print(the_new_key)
# Function that give us more info, status.
def enc_info(self):
    info_key = encinfo.info_key()
    print(info_key)

# Calling the main function to start the program.
main_cli()
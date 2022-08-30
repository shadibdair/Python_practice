# Function that decrypt the text dec
def encjsonconvert(dic, f_json, t_json):
    str_enc = ''
    with open(f_json, "r") as fm:
        str = fm.read()
        list_str = list(str)
        for letter in list_str:
            if letter in dic:
                str_enc += dic[letter]
            else:
                str_enc += letter
    with open(t_json, "w") as ft:
        ft.write(str_enc)
    return 0



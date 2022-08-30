# Function that decrypt the text dec
def encjsonconvert(dic, f_json, t_json):
    string_ = ''
    try:
        with open(f_json, "r") as fm:
            str = fm.read()
            list_str = list(str)
            for letter in list_str:
                if letter in dic:
                    string_ += dic[letter]
                else:
                    string_ += letter
        with open(t_json, "w") as ft:
            ft.write(string_)
    except FileNotFoundError as e:
        print(f"file not found: {e}")
        return 1
    except Exception as e:
        print(f"Other error {e}")
        return 1
    else:
        return 0


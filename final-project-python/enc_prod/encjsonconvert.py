# Imports
import json
#----------

def from_json(file, *more):
       with open(file, "r") as f:
        json_object = f.read()
        dic = json.loads(json_object)
        return dic["enc"], dic["dec"], dic["nameKey"]

def to_json(dic_enc, dic_dec, file, nameKey):
    dic = {"enc": dic_enc, "dec": dic_dec, "nameKey": nameKey}
    json_object = json.dumps(dic)
    with open(file, "w") as f:
        f.write(json_object)
    return 0


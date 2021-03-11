import json
filename="testdict.json"



def readDict():
 with open(filename,"rt") as f:
    item = json.load(f)
    return(item)


print(readDict())   
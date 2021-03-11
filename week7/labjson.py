import json
filename = "testdict.json"

exampleDict = dict(

name = "Mary", age = 24, grades = [1,2,3]

)

def writeDict(obj):
 with open(filename, "w") as f:
    json.dump(obj,f)  # two arguemts - the dict and the file name


writeDict(exampleDict)
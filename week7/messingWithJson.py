#json for storing data

import json


electricBill = {

"name":"Andrew",
"Amount":"999"


}

with open("storeData.json","wt") as f:
    json.dump(electricBill,f)

with open("storeData.json","rt") as f:
   readDict = json.load(f)
   print(readDict["name"])
# see if file exits

import os.path

filename = "amIhere.txt"

if (os.path.exists(filename)):
    print("files exists")
else:
    with open(filename,"x") as f:
        print("creating the file")
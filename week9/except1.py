#filename = "data.txt"

import sys

print(sys.argv)

#filename = "not.txt"

filename = sys.argv[1]  # pass in arguement in command line


try:
  with open(filename) as f:
    print(f.read())
    
 

except FileNotFoundError:
    print("file does not exist")


#raise an exception
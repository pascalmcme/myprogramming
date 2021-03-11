import os.path
filename = "count.txt"

#if not os.path.isfile(filename):
# print("File does not exist")
    


def readNumber():
    try:
        with open(filename,"rt") as f:
            number = int(f.read())
            return number
            
    
    
    except IOError:
        return 0 
         

 

print(readNumber())
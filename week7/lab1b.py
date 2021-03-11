filename="count.txt"
number=3

def writeNumber(number):
    with open(filename,"wt") as f:
        f.write(str(number))
        
    
filename="count.txt"

def readNumber():
    with open(filename) as f:
        number=int(f.read())
        return(number)

writeNumber(number)
num = readNumber()
print(num)
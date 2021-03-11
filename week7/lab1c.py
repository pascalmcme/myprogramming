filename="count.txt"


def writeNumber(number):
    with open(filename,"wt") as f:
        f.write(str(number))
        
    
filename="count.txt"

def readNumber():
    with open(filename) as f:
        number=int(f.read())   # when we write it in is string -. convert to int
        return(number)

num = readNumber()
num += 1   # number = number + 1
print("we have run this program {} times".format(num))
writeNumber(num)
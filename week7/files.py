#with open(".\lecture1.txt", "r+") as f:  # does not exist, then cannot open
   # print("create a file")


#with open(".\lecture1.txt", "w") as f:  
 #print("create a file")

with open("testdata.txt","rt") as f:
    data = f.read()
    print(data)

with open("testdata.txt","rt") as f:
    data = f.read(4)  # number of characters (new line is two characters in lenght)
    print(data)
    for line in f:
        print("we got:",line.strip())  # strip removes spaces

with open("output.txt","at") as f:  # at append , wt write
    f.write("hello \n test")
    print("my data", file=f)


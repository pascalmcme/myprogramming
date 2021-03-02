def cube(num):  # We define function cube, name of and input for the function
    return num **3  #operations

var = cube(10) 
print(var)   # var is an intent defined by input and function "cube"

for i in range(1,11):
    print(i, "cubed is: ", cube(i))
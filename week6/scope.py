var = 10

def cube(num):
 var = 66 # scope of var in functions
 print('in function',var)
 return num ** 3  

#var = cube(22) # this var is printed 
cube(22)
print('outside the cuntion',var)
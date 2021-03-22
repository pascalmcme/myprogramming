try:
 number = int(input('enter a number'))
 
 if number<0:
     raise ValueError("negative value enterted")   # create our own exception. 

 print('Number multiplied by 2 is:', number*2)

except ValueError:  # except lets you handle the error. 
    print ('please enter a positive number')
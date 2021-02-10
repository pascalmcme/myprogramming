import random
fruits = ('Apple','Banana','Pear','Grape')  # positions are 0,1,2...


index =random.randint(0,len(fruits)-1) # create a random number between 0 and 3
fruit=fruits[index]  #select item [randomnumber] from list

print('A random fruit: {}'.format(fruit))
print(index)
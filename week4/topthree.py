import random

number = random.randint(0,100)
numbers =[]


for number in range(0,10):
    number = random.randint(0,100)
    numbers.append(number)
 

print(numbers)


#https://www.programiz.com/python-programming/methods/list/sort
numbers.sort(reverse=True)

print(numbers)

top=[]
for number in range(0,3):
 top.append(numbers[number])


print(top)
import random

tennumbers = []
numberofnumbers = 10  # use this so we can easily change paramaters
rangeto = 100

for x in range(0,numberofnumbers):
    x = random.randint(0,rangeto)
    tennumbers.append(x)
 
print('Queue is ' , tennumbers)


while len(tennumbers) != 0:
     currentnumber = tennumbers.pop(0)
     print ('the current number is {} and the queue is {}' . format(currentnumber,tennumbers))

print('The queue is now empty')





'''
for x in range(0,numberofnumbers):
 tennumbers.pop(x)
 print(tennumbers)


 '''  # pop 5 does does not work - easier to use while loop.
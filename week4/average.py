numbers = []
number = int(input('Enter a number(0 to quit):'))
while number !=0:
 numbers.append(number)
 number = int(input('Enter a number(0 to quit):'))

for i in numbers:
    print(i)




Total = int(sum(numbers))
Lenght = int(len(numbers))
Average = float(Total/Lenght)

print(Average)
 
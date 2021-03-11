print("hi",55,[])



def average(*numbers):
    sumOf = sum(numbers)
    return sumOf / len(numbers)

ave = average(1,2,3,4,5,6,7,8,9)
print("average is: ",ave)
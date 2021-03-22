#[0,1,1,2,3,5,8,13,...]
#generate a sequence of lengh N
import logging
logging.basicConfig(level=logging.DEBUG)



#number = 7
numbers = []


def fibonacci(number):
    a = 0
    b = 1
    fibonacciSequence = [0]

    for i in range(1,number):
        fibonacciSequence.append(b) 
        a , b = b, a + b

    logging.debug("%d: %s",number,fibonacciSequence)

    if number == 0:
        return []
    
    if number < 0:
        raise ValueError("number must be greater than zero")


 

try:
    fibonacci(-1)
except ValueError:
    pass  # nothing happens - pass in placeholder

else: # exceuted if no value error  # 
    assert False, "fibonacci missing ValueError"

'''
return7 = [0,1,2,3,4,5,6,7,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert fibonacci(7) == return7, 'incorrect return for 7'  # we get assertion error
assert fibonacci(11) == return11, 'incorrect return for 11' # testing whether we get back what we expect. 
'''


if __name__ == "__main__": #only excecute the code below if when we are running this as the primary module. Good for testing. 
    print("all is good")


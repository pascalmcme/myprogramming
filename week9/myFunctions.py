# factorial number , 7! = 7*6*5...

def factorial(num):
    if num ==1:
        return 1
    factorial = 1
    for i in range(1,num+1):
        print("before",factorial)
        factorial *=i  # factorial = factorial * i 
        print("after",factorial)
    return factorial


#if __name__ == "__main__":
 #print("in my functions",__name__)


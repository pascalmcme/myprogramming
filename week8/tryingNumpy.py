import numpy as np

numbers = np.array([1,2,3,4,5])  #array - similar to list, all entries are of same type (int, string ect.)
print(numbers) # no commas - indicates an array 


biggerNumbers = numbers + 3

biggerNumbers = numbers * 3
print(biggerNumbers)

nbyn = numbers * numbers # muliplying vectors
print(nbyn)

randomNumbers = np.random.randint(100,200,5) #(start,end,count)
print(randomNumbers)

randomNumbers = np.random.normal(size = 100) 
print(randomNumbers)
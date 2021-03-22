import numpy as np
import matplotlib.pyplot as plt  #https://matplotlib.org/ for help

'''
np.random.seed(1)  # same random numbers every time
normData = np.random.normal(size = 1000)


plt.hist(normData)
plt.show()
'''


fruit = np.array(['apples','oranges','pears'])
numbers = np.array[(23,77,500)]

plt.pie(numbers, labels = fruit)
plt.show()
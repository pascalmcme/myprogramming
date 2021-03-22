import numpy as np
import matplotlib.pyplot as plt



minsalary = 20000
maxsalary = 80000
entries = 100

np.random.seed(1)
salaries = np.random.randint(minsalary,maxsalary,entries)  # makes an array



plt.hist(salaries,25)  # added bins paramater (how x is grouped)
plt.show()

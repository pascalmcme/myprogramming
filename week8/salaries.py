import numpy as np
import matplotlib.pyplot as plt



minsalary = 20000
maxsalary = 80000
entries = 10

np.random.seed(1)
salaries = np.random.randint(minsalary,maxsalary,entries)  # makes an array
salaries = salaries + 5000
salaries = salaries * 10.05
print(salaries)
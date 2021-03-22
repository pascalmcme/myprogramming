import numpy as np
import matplotlib.pyplot as plt  #https://matplotlib.org/ for help


minsalary = 20000
maxsalary = 80000
entries = 100


np.random.seed(1)
salaries = np.random.randint(minsalary,maxsalary,entries)

np.random.seed(1)
age = np.random.randint(low = 21 , high = 65, size = entries)

plt.scatter(age,salaries,color = 'green')
plt.title("Salaries by Age")
plt.xlabel("age")
plt.ylabel("salaries")
plt.legend()
plt.show()

plt.savefig("veryniceplot.png")
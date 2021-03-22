import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101)) 
ypoints = xpoints * xpoints
plt.plot(xpoints, ypoints)
#plt.show()
#plt.legend( )  # add a legend
plt.savefig('lecture1.png')


randompoints = np.random.randint(1,1000,100)
plt.scatter(xpoints, randompoints)
plt.show()
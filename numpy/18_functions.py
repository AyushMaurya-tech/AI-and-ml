#unique
import numpy as np
var = np.array([1,2,4,2,4,53,53,65])
x = np.unique(var,return_index = True,return_counts=True)
print(x)
#resize
y = np.resize(var,(2,4))
print(y)
#flatten
print(y.flatten(order="f"))
#we can change the fucking orders
print(np.ravel(y))
#flatten and ravel are same shit
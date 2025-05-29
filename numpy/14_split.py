import numpy as np
var = np.array([1,2,3,43,5325,334])
print(var)
ar = np.array_split(var,4)
print(ar)
var1 = np.array([[1,2],[2,4],[3,4]])
print(np.split(var1,3))
print(np.split(var1,2,axis=1))
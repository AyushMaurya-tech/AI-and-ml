import numpy as np
var = np.array([1,2,3,4])
var1 = np.array([1,2,342,3])
arc = np.concatenate((var,var1))
print(arc)
#2 dim
var2 = np.array([[1,2],[2,3]])
var3 = np.array([[2,3],[3,4]])
print(np.concatenate((var2,var3),axis=1))
var2 = np.array([[1,2],[2,3]])
var3 = np.array([[2,3],[3,4]])
print(np.concatenate((var2,var3),axis=0))


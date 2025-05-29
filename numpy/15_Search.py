import numpy as np
var = np.array([1,2,3,4,4,5,6,4,3245,2,31,3,2])
x = np.where((var%2)==0)
y = np.sort(var)
print(x)
print(y)
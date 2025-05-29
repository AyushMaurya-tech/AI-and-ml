import numpy as np
a = np.array([1,2,3])
print(a)
print(a.ndim)# for dim of array
print(type(a))
b = np.array([[1,2,3,4],[1,2,3,4]])
print(b)
print(b.ndim)
c = np.array([(1,2,3,4)],ndmin = 10)#multidimension array
print(c)
print(c.ndim)
ar_zero = np.zeros(4)
print(ar_zero)
print(np.zeros((3,4)))
print(np.ones((3,4)))
print(np.empty(4))
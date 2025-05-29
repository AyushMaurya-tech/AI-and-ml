import numpy as np
var1 = np.array([1,2,3,4])
var2 = np.array([9,8,7,6])
a_new = np.stack((var1 , var2),axis=1)
a_new1 = np.hstack((var1,var2))#row
a_new2 = np.vstack((var1,var2))#columns
a_new3 = np.dstack((var1,var2))#height
print(a_new)
print()
print(a_new1)
print()
print(a_new2)
print()
print(a_new3)
print()
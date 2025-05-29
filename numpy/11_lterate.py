import numpy as np
var = np.array([1,2,3,4,5])
for i in var:
    print(i)
var2 = np.array([[1,2,3,5],[2,24,4,2],[2,0,0,0],[4,0,0,0]])
for i in var2 :
    for k in i:
        print(k)
for i in np.nditer(var2):
    print(i)
#for changing its data type
for i in np.nditer(var2,flags = ["buffered"],op_dtypes=["S"]):
    print(i)
for i in np.ndenumerate(var2):
    print(i)
import numpy as np
var = np.array([1,2,4,2,4,53,53,65])
#v = np.insert(var ,(2),40)
v = np.append(var,6)

#if we give float value then it won't work
print(var)
print(v)
print("///////")
var1 = np.array([[1,2,3],[1,5,4]])
print(var1)
print(np.insert(var1,2,6,axis=1))
# print(np.append(var1,[[45],[54]],axis=1))
print("//////")
print(np.delete(var,2))
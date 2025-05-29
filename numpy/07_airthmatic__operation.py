import numpy as np
var = np.array([1,2,3,4,5,6])
varadd = var + 3
print(varadd)
var1 = np.array([1,2,3,4,5,6])
varadd1 = var+var1
print(varadd1)
print(np.max(var),np.argmax(var))
print(np.min(var),np.argmin(var))

# as this we can do anything like divide substract and 
# modulus
#we can use function like 
#np.add(a,b)
#np.substract(a,b)
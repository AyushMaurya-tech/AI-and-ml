import numpy as np
var = np.array([1,2,4,3,65,4545,4])
co = var.copy()
print(var)
print(co)
vi = var.view()
print(vi)
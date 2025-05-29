import pandas as pd
var1 = pd.DataFrame({"A":[1,2,3,4],"b": [4,5,3,4]})
print(var1)
print(var1["A"]+var1["b"])
var1["python"] = var1["A"]>=3
print(var1)
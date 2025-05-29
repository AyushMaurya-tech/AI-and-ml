import pandas as pd 
var = pd.DataFrame({"a":[1,2,3,4,5],"b":[5,2,5,3,4]})
var.pop("a")
print(var) 
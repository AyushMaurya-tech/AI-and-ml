import pandas as pd 
var = pd.DataFrame({"a":[1,2,3,4,5],"b":[5,2,5,3,4]})
var.insert(1,"python",var["a"])
print(var)
print("///////")
var.insert(3,"pandas",[1,2,3,4,5])
print(var)
print("////////")
var["python_12"] = var["a"][0:3]
# cant convert becase cant convert nan
# convert_dict = {'a':int,'b':int,'pandas':int,'python_12':int}
# var = var.astype(convert_dict)
print(var)
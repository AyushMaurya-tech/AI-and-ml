#we can pass anything in this series like dict,list,touple etc.
import pandas as pd
x = [3,4,5,6,7]
var = pd.Series(x,dtype=float)
print(var)
print(type(var))
print("////////////////")
dic = {"name":['python','c','c++','java'],"por":[12,14,13,14],"rank":[1,2,35,2]}
print(pd.Series(dic)) 
print("////////////////")
print(pd.Series(123))
import pandas as pd
#in pandas brodcast rule is not important\
x = [3,4,5,6,7]
var = pd.Series(x,dtype=float)
var1 = pd.Series([1,5,2,3,24,5,2,4,24],dtype="int64")
print(var + var1)
# it will give fiurther nan meanks not a number
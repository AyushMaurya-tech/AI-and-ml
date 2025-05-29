import pandas as pd
dls = {"a":[1,23,4,5,6],"b":[42,3,5,3,3],"c":[65,34,23,43,67]}
d = pd.DataFrame(dls)
print(d)
d.to_csv("test.csv")
d.to_csv("test_1.csv",index=False)
d.to_csv("test_2.csv",index=False,header=[1,2,3])
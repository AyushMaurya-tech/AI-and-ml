import pandas as pd
x= [1,45,5,4,3,554,543,4]
print(pd.DataFrame(x))
print("///////////////")
d = {"a":[1,4,3,2,4,2],"s":[1,3,5,3,45,56],1:[1,2,3,54,34,43]}
# both typle should be of same length
print(pd.DataFrame(d))
print("///////////////")
t = pd.DataFrame(d,columns=["a",1],index=["a","b","c","d","e","F"])
print(t)

print("///////////////")
print(d["a"][3])
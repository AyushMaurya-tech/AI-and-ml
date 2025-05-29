import pandas as pd
csv_1 = pd.read_csv("E:\\ML and AI\python\pandas\c.csv")
print(csv_1)
#only row
csv_2 = pd.read_csv("E:\\ML and AI\python\pandas\c.csv",nrows=1)
print(csv_2)
print(type(csv_2))
#get cols
csv_3 = pd.read_csv("E:\\ML and AI\python\pandas\c.csv",usecols=["Customer Id","First Name"])
print(csv_3)
#row skipping
csv_4 = pd.read_csv("E:\\ML and AI\python\pandas\c.csv",usecols=["Customer Id","First Name"],skiprows=[1])
print("abcd")
print(csv_4)
#change index
csv_5 = pd.read_csv("E:\\ML and AI\python\pandas\c.csv",index_col="Phone 2")
print("abcd34567")
print(csv_5)
#header
csv_6 = pd.read_csv("E:\\ML and AI\python\pandas\c.csv",header=2)
print("abcdhfsfufnerfir")
print(csv_6)
#change header if aint there
col = ["col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12"]



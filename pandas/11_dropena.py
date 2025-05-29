import pandas as pd
csv_1 = pd.read_csv("E:\ML and AI\python\pandas\data_with_nan.csv")
print(csv_1)
x = csv_1.dropna()
print("/////\\\\\\")
#it will drop along row of nan value
print(x)
#dropping along column
print("\]\]\]")
y = csv_1.dropna(axis=1)
print(y)
print("xxxxxx")
#if complete row is nan
print(csv_1.dropna(how="all"))
print("klklklklk")
#along particular column removing nan
print(csv_1.dropna(subset=["City"]))


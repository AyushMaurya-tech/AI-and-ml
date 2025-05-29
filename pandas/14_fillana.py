import pandas as pd
csv_1 = pd.read_csv("E:\\ML and AI\\python\\pandas\\data_with_nan.csv")
print(csv_1.fillna("pytho",limit=1))#in column only one na will be replaced bcause limit is one
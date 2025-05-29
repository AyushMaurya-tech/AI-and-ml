import pandas as pd
csv_1 = pd.read_csv("E:\\ML and AI\\python\\pandas\\data_with_nan.csv")
#print(csv_1.fillna("pytthon")) it will fill nan as pythhon
#print(csv_1.fillna({"Name":"bab","Age":"buajd","Score":"bbc","City":"nmn"}))#change according to column
print(csv_1.fillna(method = "ffill"))# for nan got fillege by its backword and forward values
# bfill for backward fill
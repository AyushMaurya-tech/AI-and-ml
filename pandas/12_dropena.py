import pandas as pd
csv_1 = pd.read_csv("E:\\ML and AI\\python\\pandas\\data_with_nan.csv")
print(csv_1.dropna(inplace=True))#in this it will remove all nan value row

#print(csv_1.dropna(thresh=1)) #it will remove wheneverv single nan

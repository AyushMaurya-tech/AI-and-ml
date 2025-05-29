import pandas as pd
csv_1 = pd.read_csv("E:\ML and AI\python\pandas\c.csv")
csv_1.loc[0,"Customer Id"] = "python"
print(csv_1)
print(csv_1.loc[[2,3],["Customer Id","First Name"]])
print(csv_1.loc[:,["Customer Id","First Name"]])
print("eoiei")
print(csv_1.iloc[0,2])
#how to remove
x = csv_1.drop("Customer Id",axis=1)
print(x)
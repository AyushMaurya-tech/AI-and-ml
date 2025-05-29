import pandas as pd
csv_1 = pd.read_csv("E:\ML and AI\python\pandas\c.csv")
print(csv_1)
print("abcdefg")
print(csv_1.index)
print(csv_1.columns)
print("abcdefghijklmnop")
print(csv_1.describe())
print("abcdefghijklmn")
print(csv_1.head(6))
print("ayush")
print(csv_1.tail(5))
print("cjdnjen")
print(csv_1[:9])
#converting in numpy array
x = csv_1.to_numpy
print("ppppppp")
print(x)
print("P")
#sorting
#axis = 0 means sorting accorting row
# and 1 for column sorting
print(csv_1.sort_index(axis=0,ascending=False))
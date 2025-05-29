import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.title('gas prices overtime')
gas = pd.read_csv('E:\ML and AI\python\matplotlib\gas_prices.csv')
print(gas)
plt.plot(gas.Year,gas.USA,'blue',label = 'USA',marker=".")
plt.plot(gas.Year,gas.Italy,label = "black",marker = '*')
plt.plot(gas.Year,gas.Canada,label = 'Canada',marker = '^')
plt.xticks(gas.Year[::3])
plt.yticks([0,1,2,3,4,5,6,7,8,9])
plt.xlabel("year")
plt.ylabel("USD")
plt.legend()
plt.savefig("gas_price.png",dpi = 300)
plt.show()
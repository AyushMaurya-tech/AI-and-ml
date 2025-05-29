import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.figure(figsize=(3,2),dpi = 300)
value = [5,8,3,9]
label = ["a","b","c","d"]
bar = plt.bar(label,value)
bar[0].set_hatch('O')
bar[1].set_hatch('*')
bar[2].set_hatch('/')
bar[3].set_hatch('P')
plt.title('our second plot',fontdict={'fontname':'Comic sans MS','fontsize':20})
plt.savefig('mygraph1.png',dpi = 300)
plt.show()
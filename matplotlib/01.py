import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x = [0,1,2,3,4]
y = [0,2,4,6,8]
#size fixing of graph
plt.figure(figsize=(4,3),dpi = 300)
#select interval
x2 = np.arange(0,4.5,0.5)
#plot part of the graph as line
plt.plot(x2[0:6],x2[0:6]**2,'red',label = 'x^2')
#plotting as dash
plt.plot(x2[5:],x2[5:]**2,'r--')
#line 2
#keywords
plt.plot(x,y,'b^--',label='2x',color = 'blue',linewidth = 2,marker = '.',linestyle = '--', markersize = 10,markeredgecolor = 'black')
plt.xlabel('x label')
plt.ylabel('y label',fontdict={'fontname':'Comic Sans MS'})
plt.title('our first plot',fontdict={'fontname':'Comic sans MS','fontsize':20})
plt.xticks([0,1,2,3,4])
plt.yticks([2,4,6,8,10,12,14,16,18])
#for adding legend meaning showing equation
plt.legend()
#for saving
plt.savefig('mygraph.png',dpi = 300)
plt.show()
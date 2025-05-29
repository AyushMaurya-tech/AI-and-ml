import matplotlib.pyplot as plt
import pandas as pd
# Load the CSV file into a DataFrame (use raw string or double backslashes for path)
fifa = pd.read_csv(r"E:\ML and AI\python\matplotlib\fifa_data.csv")
left = fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]
labels = ['Left','Right']
colours = ['#abcdef','#aabbcc']

plt.pie([left,right],labels = labels,colors=colours,autopct='%.2f')
plt.legend()
plt.title('Foot Preference of FIFA Players')
plt.show()
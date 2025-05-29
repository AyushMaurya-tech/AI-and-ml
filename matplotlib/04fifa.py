import matplotlib.pyplot as plt
import pandas as pd
# Load the CSV file into a DataFrame (use raw string or double backslashes for path)
fifa = pd.read_csv(r"E:\ML and AI\python\matplotlib\fifa_data.csv")
# Print the first few rows of the dataframe to inspect the data
print(fifa.head())
bins = [40,50,60,70,80,90,100]
# Plot histogram of the 'Overall' column
plt.hist(fifa.Overall, bins= bins, edgecolor='black',color="#781781")
plt.xticks(bins)
plt.title('Distribution of FIFA Player Overall Ratings')
plt.xlabel('Overall Rating')
plt.ylabel('NUmber of players')
print(fifa['Preferred Foot'])
plt.show()


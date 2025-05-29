import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')

# Load the CSV file into a DataFrame
fifa = pd.read_csv(r"E:\ML and AI\python\matplotlib\fifa_data.csv")

# Define the labels
labels = ["FC Barcelona", "Real Madrid", "New England Revolution"]

# Extract data for the clubs
barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']  # Fixed extra space issue

# Create the boxplot
plt.boxplot([barcelona, madrid, revs], labels=labels)

# Add a title and axis labels
plt.title('Overall Player Ratings by Club')
plt.ylabel('Overall Rating')

# Show the plot
plt.show()

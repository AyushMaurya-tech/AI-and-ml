import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('ggplot')
# Load the CSV file into a DataFrame (use raw string or double backslashes for path)
fifa = pd.read_csv(r"E:\ML and AI\python\matplotlib\fifa_data.csv")
print(fifa.Weight)
fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
light = fifa.loc[(fifa.Weight<=125)].count()[0]
light_medium = fifa.loc[(fifa.Weight>=125)&(fifa.Weight<150)].count()[0]
medium = fifa.loc[(fifa.Weight>150)&(fifa.Weight<175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight>175)&(fifa.Weight<200)].count()[0]
heavy = fifa.loc[(fifa.Weight>=200)].count()[0]
weight = [light,light_medium,medium,medium_heavy,heavy]
explode = (.4,.2,0,0,.4)
plt.title('weight distribution in fifa')
plt.pie(weight,labels= ['under 125','125-150','150-175','175-200','obove 200'],autopct='%.2f %%',pctdistance=0.8,explode=explode)
plt.show()
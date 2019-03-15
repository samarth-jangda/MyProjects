# The following projectis based on analysis of total deaths in countries and India

#So we first going to import pandas (library of python)
import pandas as pd
from numpy import nan
import matplotlib.pyplot as plt
#After that give the file location
deaths = pd.read_csv("C:\\Users\\LENOVO\\Documents\\Hack@HMR.csv")
#then we are going to print the following data
deaths.replace(nan, 0, inplace = True)

for column in ["World-deaths", "India-deaths"] :
    deaths[column] = deaths[column].map(lambda x : int(x.replace(",", "")))
#After that we will be plotting the graph
plt.clf()          # clf is clear data frame
# plt.figure(figsize = (18, 14), dpi=120)

# Preparing bars for Average DR
barDR = plt.bar(deaths["Diseases"], deaths["India-deaths"], width = 0.75, align = 'center', color = 'green',
                label = 'Diseases')                                      #This will plot bar graph

# Setting graph properties
# plt.yticks(range(0, 6000, 250))
# plt.xticks(range(len(deaths["Diseases"])), deaths["Diseases"])
plt.ylabel("India-deaths")               # The labling of y axis will be here
plt.xlabel("Diseases")                   # The labeling of x axis will be here
plt.title("Deaths in India due to Disease")   #  This will give the title to the plot
plt.legend(fontsize='small')
plt.grid()                           # This gives the grid in the graph
# for (rect, label) in zip(barDR, yrly_avg_DR[-1::-1]):
#     plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 150, format(label, '.2f'), ha='center', va='top')
# In order to show the whole graph use:
plt.show()
# Then print the deaths
print(deaths)

# Now I am going to print another dataset of deaths due to major diseases in every country
#for that we are going to use pandas
diseases = pd.read_csv("C:\\Users\\LENOVO\\Documents\\Deaths(1).csv")

print(4)
print(diseases)

plt.clf()          # clf is clear data frame
# plt.figure(figsize = (18, 14), dpi=120)

# Preparing bars for Average DR
barDR = plt.bar(diseases["Country"], diseases["Heart"], width = 0.75, align = 'center', color = 'green',
                label = 'Diseases')                                      #This will plot bar graph

# Setting graph properties
# plt.yticks(range(0, 6000, 250))
# plt.xticks(range(len(deaths["Diseases"])), deaths["Diseases"])
plt.ylabel("Heart Disease")               # The labling of y axis will be here
plt.xlabel("Country")                   # The labeling of x axis will be here
plt.title("Deaths in every country due to heart Disease")   #  This will give the title to the plot
plt.legend(fontsize='small')
plt.grid()                           # This gives the grid in the graph
# for (rect, label) in zip(barDR, yrly_avg_DR[-1::-1]):
#     plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 150, format(label, '.2f'), ha='center', va='top')
# In order to show the whole graph use:
plt.show()
# Then print the deaths
print(diseases)
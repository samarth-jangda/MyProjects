#Firstly import pandas
import pandas as pd
#Then give the file location
Samsung_data = pd.read_csv("/Users/LENOVO/Documents/Project2.csv")   #In the data IM stands for(information tachnology and mobile development)
print(Samsung_data)      #Print the result of the data               #and CE stands for(consumer engineering)
#Then import matplotlib
import matplotlib.pyplot as plt
#Then give the data to be plotted on the graph
Earnings = [4.8,8.9,10.7,7.2,7.4,8.1,14.5]
Sales = [48,56,59,53,53,54,67]
width = 5
#Then plot the graph
plt.bar(Earnings,Sales , color = "r", width = 0.1)
#After that label your x and y data
plt.xlabel("Earnings are present in billions")
plt.ylabel("Sales are present in trillions")
#Then provide the range to x and y axis
plt.xticks(range(4,15,2))
plt.yticks(range(10,70,
                 ))
#Finally display the plot
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import nan
import seaborn as sns

#1
df = pd.read_csv("C:\\Users\\Samarth\\Desktop\\2.5NVG.csv")
df.replace(nan,float(0.0),inplace = True)
print(df)
cdf = df[["Gap period","Duration","Initial Investment","NVG person visit","Orders to NVG","Orders to Non NVG","Ratio",
          "Family size","Average Profit","Local shops"]]
#cdf["Duration"] = cdf["Duration"].map(lambda x : int(x))
print(cdf)
plt.clf()
plt.figure(figsize=plt.figaspect(2.0))
plt.bar(x ='Gap period',color="brown",data=cdf,height = 20,width = 1.02,label = "Gap period")
plt.bar(x = "NVG person visit",color = "orange",data = cdf,height= 20,width = 1.02,label = "NVG person visit")
plt.legend(cdf,fontsize = 8)
plt.grid()
plt.title("Gap period and NVG person visit")
plt.show()

#2)
plt.clf()
sns.lineplot(x = 'Gap period',y = "Initial Investment",color = 'red' ,data = cdf,linewidth = 1.0)
sns.lineplot(x = "Gap period",y = "NVG person visit",color="black",data=cdf)
sns.lineplot(x = 'Gap period',y = "Initial Investment",color = 'red' ,data = cdf)
sns.lineplot(x = "Gap period",y = "NVG person visit",color="black",data=cdf)
plt.grid()
plt.legend(cdf,fontsize = 8)
plt.show()



#3)
cdf["Duration"] = cdf["Duration"].map(lambda x : int(x))
plt.clf()
sns.barplot(x ="Family size",y = "Initial Investment",color ="purple",data = cdf)
plt.grid()
plt.tight_layout()
sns.barplot(x = "Duration",y = "Initial Investment",color = "brown",data = cdf)
#plt.legend(cdf,fontsize = 10)
plt.tight_layout()
plt.subplots_adjust(left =0.125,right =0.9,hspace=0.3,wspace=0.4)
plt.grid()
plt.show()
tdf = pd.read_csv("C:\\Users\\Samarth\\Desktop\\2.5NVG_3.csv")
tdf.replace(nan,str(0),inplace=True)
print(tdf)
plt.clf()
#plt.(x ='Gap period',y = "Initial Investment",color = "black",data = cdf)
sns.lineplot(x = "Duration",y = "Initial Investment",color = "black",data = cdf)
plt.plot("Duration","Initial Investment",'o')
plt.grid()
plt.show()

df_1 = df["Duration"].value_counts()
print(df_1)

#4
plt.clf()
cdf["Initial Investment"] = cdf["Initial Investment"].map(lambda x : int(x))

g = sns.pairplot(cdf,x_vars=["Gap period","Duration"],y_vars=["Initial Investment","NVG person visit"],kind="bar",)
g = g.map(plt.hist2d)
plt.show()
g = sns.FacetGrid(df, col="NVG person visit", hue="VSE ",hue_kws={"marker" : ["^","+","v"]},)
g.map(plt.scatter, "Average Profit", "Family size", alpha=.7,linewidth = 4.5,edgecolor = "red")
g.add_legend()
g.fig.subplots_adjust(wspace=.02, hspace=.02)
plt.show()

#5
plt.clf()
#df["Orders to NVG"] = df["Orders to NVG"].map(lambda x : int(x))
a = sns.FacetGrid(df,col = "Orders to Non NVG",hue = "Professional linkage")
a.map(plt.scatter,"Orders to Non NVG","Orders to NVG",alpha = .7,linewidth = 1.5,edgecolor = "red")
a.add_legend()
g.fig.subplots_adjust(wspace = .02, hspace = .02)
plt.show()

#6
cdf["Orders to Non NVG"] = cdf["Orders to Non NVG"].map(lambda x : int(x))
b = sns.heatmap(cdf,vmin="Orders to Non NVG",vmax="Orders to Non NVG",linecolor="blue")
plt.show()

#df_2 = pd.read_csv("C:\\Users\\Samarth\\Desktop\\New Data.csv")
#with open("C:\\Users\\Samarth\\Desktop\\New Data.csv", encoding="utf8", errors='ignore') as f:
#    print(df_2)
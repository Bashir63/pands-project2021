import pandas as pd
from pandas import DataFrame
import numpy as np
from numpy import array
import seaborn as sns
import matplotlib.pyplot as plt 


with open ("DATA/irisdata.csv") as ds: 
    cols = ["Sepal Length", "Sepal Width" , "Petal Length", "Petal Width", "Species"]
    data = pd.read_csv(ds, names=cols)

'''                      Scatter Plots                           '''
sns.set()    
data.plot(kind="scatter", x="Sepal Length", y="Sepal Width", figsize = (10, 7))
plt.title("Scatter Plot")   
plt.show()                  

sns.set()   
data.plot(kind="scatter", x="Petal Length", y="Petal Width", figsize = (10, 7))
plt.title("Scatter Plot")  
plt.show()                 


'''                 #Histograms            '''                                                   

sns.set_style("darkgrid")      # Use seaborn on background
plt.figure(figsize = (10, 7))  # Adjust the size of the graph
x = data["Sepal Length"]       # Find the Sepal Length and store in x
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram - Sepal Length(cm)")# Title of graph
plt.xlabel("Sepal_Length_cm")       # Xlabel 
plt.ylabel("Count")                 # Ylabel
plt.grid(True)
plt.savefig("Plot1.png")

sns.set()                       # Use default seaborn on background
plt.figure(figsize = (10, 7))   # Adjust the size of the graph
x = data["Sepal Width"]         # Find the Sepal Length and store in x
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram- Sepal Width (cm)")# Title of graph
plt.xlabel("Sepal_width_cm")            # Xlabel 
plt.ylabel("Count")                     # Ylabel
plt.savefig("Plot2.png")

sns.set()                       # Use default seaborn on background
plt.figure(figsize = (10, 7))   # Adjust the size of the graph
x = data["Petal Length"]        # Find the Sepal Length and store in x
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram - Petal Length(cm)")# Title of graph
plt.xlabel("Petal_Length_cm")            # Xlabel 
plt.ylabel("Count")                     # Ylabel
plt.savefig("Plot3.png")

sns.set()                       # Use default seaborn on background
plt.figure(figsize = (10, 7))   # Adjust the size of the graph
x = data["Petal Width"]         # Find the Sepal Length and store in x
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram - Petal Width(cm)")# Title of graph
plt.xlabel("Petal_Width_cm")            # Xlabel 
plt.ylabel("Count")                     # Ylabel 
plt.savefig("Plot4.png")


                    
# Load the Pandas Libraries with the alias of pd
import pandas as pd
from pandas import DataFrame

# Load the NumPy Libraries with the alias of np
import numpy as np
from numpy import array

# statistical data visualization 
import seaborn as sns
import matplotlib.pyplot as plt 


# Open the CSV file and call is ds. We also will add headings to each column and print the results. 
with open ("DATA/irisdata.csv") as ds: 
    cols = ["Sepal Length", "Sepal Width" , "Petal Length", "Petal Width", "Species"]
    data = pd.read_csv(ds, names=cols)
print(data)
print("\n")


# Display the amount of rows and columns in the set
print(data.shape)
print("\n")


# Print the unique values of the data set and display the number of rows that belong to each
data['Species'].unique()
print(data.groupby('Species').size())
print("\n")


# Summary of each attribute
print(data.describe())
print("\n")


'''                      Scatter Plots                           '''
# Scatter Plot with x and y axis defined
sns.set()    # Use seaborn to add style ie Graph
data.plot(kind="scatter", x="Sepal Length", y="Sepal Width", figsize = (10, 7))
plt.title("Scatter Plot")   # Title of graph
plt.show()                  # Show graph

# Scatter Plot with x and y axis defined
sns.set()    # Use seaborn to add style ie Graph
data.plot(kind="scatter", x="Petal Length", y="Petal Width", figsize = (10, 7))
plt.title("Scatter Plot")   # Title of graph
plt.show()                  # Show graph




#Histograms                                                   

# Histagram for Sepal Length
 #plt.grid(True)               # Used sns.set instead to display the grid and set a background color
sns.set_style("darkgrid")      # Use seaborn on background
plt.figure(figsize = (10, 7))  # Adjust the size of the graph
x = data["Sepal Length"]       # Find the Sepal Length and store in x
# Bin based on Sepal Length
# Bins are set to 10 by default. I have included is for view purposes
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram - Sepal Length(cm)")# Title of graph
plt.xlabel("Sepal_Length_cm")       # Xlabel 
plt.ylabel("Count")                 # Ylabel
plt.grid(True)
plt.savefig("Plot1.png")

# Histagram for Sepal Width
 #plt.grid(True)                # Used sns.set instead to display the grid and set a background color
sns.set()                       # Use default seaborn on background
plt.figure(figsize = (10, 7))   # Adjust the size of the graph
x = data["Sepal Width"]         # Find the Sepal Length and store in x
# Bin based on Sepal Length
# Bins are set to 10 by default. I have included is for view purposes
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram- Sepal Width (cm)")# Title of graph
plt.xlabel("Sepal_width_cm")            # Xlabel 
plt.ylabel("Count")                     # Ylabel
plt.savefig("Plot2.png")

# Histagram for Petal Length
 #plt.grid(True)                # Used sns.set instead to display the grid and set a background color
sns.set()                       # Use default seaborn on background
plt.figure(figsize = (10, 7))   # Adjust the size of the graph
x = data["Petal Length"]        # Find the Sepal Length and store in x
# Bin based on Sepal Length
# Bins are set to 10 by default. I have included is for view purposes
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram - Petal Length(cm)")# Title of graph
plt.xlabel("Petal_Length_cm")            # Xlabel 
plt.ylabel("Count")                     # Ylabel
plt.savefig("Plot3.png")

# Histagram for Petal Width
 #plt.grid(True)                # Used sns.set instead to display the grid and set a background color
sns.set()                       # Use default seaborn on background
plt.figure(figsize = (10, 7))   # Adjust the size of the graph
x = data["Petal Width"]         # Find the Sepal Length and store in x
# Bin based on Sepal Length
# Bins are set to 10 by default. I have included is for view purposes
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram - Petal Width(cm)")# Title of graph
plt.xlabel("Petal_Width_cm")            # Xlabel 
plt.ylabel("Count")                     # Ylabel 
plt.savefig("Plot4.png")


                    
# Load the Pandas Libraries with the alias of pd
import pandas as pd
from pandas import DataFrame

# Load the NumPy Libraries with the alias of np
import numpy as np
from numpy import array

# statistical data visualization 
import seaborn as sns
import matplotlib.pyplot as plt


#When using the below code to view the data will work but wont have headings See the with open section for the update. 
#Update on this is that I had to add a line naming the columns. See line 11 

'''# Load the CSV file
f = pd.read_csv("DATA/irisdata.csv")
f.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species'] 
# Print the contents of the CSV file
print(f)'''



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



'''                                 Histograms                                                   '''
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
plt.show()                          # Show graph


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
plt.show()                              # Show graph


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
plt.show()                              # Show graph


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
plt.show()                              # Show graph


#The four histograms together.
data.hist(bins = 20, figsize = (10, 7))  # Display graphs and resize window
plt.grid(True)        # Display a grid
plt.show()            # Show graph





'''                      Scatter Plots                           '''
# Scatter Plot with x and y axis defined
sns.set()    # Use seaborn to add style ie Graph
data.plot(kind="scatter", x="Sepal Length", y="Sepal Width", figsize = (10, 7))
plt.title("Scatter Plot")   # Title of graph
plt.show()                  # Show graph


'''# Scatter Plot with x and y axis defined with color
sns.set_style("whitegrid")    # Use seaborn to add whitegrid background
# Colour(hue) by Species, plot scatter plot on sepal length(X-Axis) and width(Y-Axix)
sns.FacetGrid(data, hue="Species", size=7) \
    .map(plt.scatter, "Sepal Length", "Sepal Width" ) \
    .add_legend()  # Add a legend to define what colour belongs to each species
plt.title("Scatter Plot With Colour")   # Title of graph
plt.show()  '''                            # Show graph


# scatter plot matrix

sns.set(style="ticks")    # Use seaborn to add style ie Graph
sns.pairplot(data, hue="Species", size =2) # Plot data elements in different colour 
plt.show()   # Show graph
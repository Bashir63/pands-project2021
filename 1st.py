import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

# Rading the csv data file, assigning variable to its content
# Attribute `header=None` assumes that there is no header line in the raw csv file - the first row is actual data
ids = pd.read_csv("DATA/irisdata.csv", header=None)  # ids - iris data set

# Adding headers to attributes (columns); source: https://stackoverflow.com/a/28162530
# SL - sepal length, SW - sepal width, Petal length, Petal width; all measurements in cm; class is one of 3 iris species
ids.columns = ["SL", "SW", "PL", "PW", "Species"]

# Content of the data (commented out for clarity - too long)
# print(ids) # commented out for clarity only

# head and tail methods print out n first / last respectively lines of data, where n is an argument of the method, default argument is n=5; source: http://www.datasciencemadesimple.com/head-and-tail-in-python-pandas/
print(ids.head())
# print(ids[49:51]) # This shows rows of index between 49 and 51 (incl. 49 bu excl. 51), where there is a change in the iris specie in the data set
# print(ids[99:101]) # Shows rows index between 100 and 101
print(ids.tail(3))

# Application of .describe() method - shows basic statistical information of the data set
print(ids.describe())

# Histogram of the entire data set, not discriminating the species
# ids.hist() # commented out for clarity only
# pl.show() # commented out for clarity only

# Separation of the data per attributes (columns)
# Confirming the type of the data set
# firstcol = ids[:, 0] # this command would produce a TypeError. Currently data type is DataFrame (consists of numbers and strings), meaning it cannont be sliced
# print(type(ids)) # confirming the data type - commented out for clarity

# Pandas command `groupby` allows for separating the data set by attribut (of the function) passed in the attribute (of the method); source https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
print(ids.groupby('Species').size())


# Split-out validation dataset; source https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
# changes datatype to `ndarray` and separates the columns with numerical values (first 4 columns); idsv - iris data set values
idsv = ids.values[:, 0:4]
# print(type(idsv)) # confirming the data type - commented out for clarity
# separates the last column with the species names (50 setosas, 50 versicolors and 50 virginicas)
spec_names = ids.values[:, 4]
# print(type(spec_names)) # confirming the data type - commented out for clarity
# print(Y)

# Further separation - slicing by attribute and species - first attributer of first 50 instances - sepal length of Iris Setosa
sepal_l_setosa = idsv[0:49, 0]
# minimum value of the subset, see next cell for results
sels_min = np.min(sepal_l_setosa)  # minimum value of the subset
sels_mean = np.mean(sepal_l_setosa)  # mean value of the subset
sels_max = np.max(sepal_l_setosa)  # maximum value of the subset
print(sels_min, sels_mean, sels_max)

#  print(sepal_l_setosa)

# histogram
# pl.hist(sepal_l_setosa)
# pl.show

print(ids.columns)

# 2-D scatter plot; source: https://youtu.be/FLuqwQgSBDw?t=1069
# idsv.plot(kind="scatter", X="Sepal length, cm", Y="Sepal width, cm")
# pl.show()

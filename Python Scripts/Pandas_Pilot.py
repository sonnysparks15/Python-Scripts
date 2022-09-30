###################################################
# Pandas Pilot
# Edwin (Sonny) Sparks
# April 24,, 2022
###################################################

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

####################################################
# Pandas #
###############################
# Pandas Series #
series = pd.Series([10, 20, 30, 40], ['A', 'B', 'C', 'D'])
# 1st is Value collection, 2nd is Index collection by default #

print(series['C'])
series.name = 'My Series'
s1 = pd.Series([1, 2, 3, 4], ['a', 'b', 'c', 'd'])
s2 = pd.Series([7, 5, 1, 2], ['a', 'b', 'c', 'd'])
print(s1 + s2)

print(s1.count())  # Number of elements
print(s1.head())  # Head of data frame
print(s1.tail())  # Tail of data frame


def mysquare(x):
    return x ** 2


print(s1.apply(mysquare))  # Applying a function to series
print(s1.sort_index())  # Sort Series

s1.plot()  # Plotting Series
plt.show()  # Showing plot

#####################
# Data Frames #
#####################
data = {
    'SSN': [123, 445, 511, 872],
    'Name': ['Anna', 'Bob', 'John', 'Mike'],
    'Age': [29, 43, 82, 23],
    'Height': [176, 165, 187, 182],
    'Gender': ['f', 'm', 'm', 'f']
}
df = pd.DataFrame(data)
df.set_index('SSN', inplace=True)  # Inplace=True applies to current dataframe

print(df.ndim)  # Dataframe dimensions
print(df.shape)  # Dataframe shape
print(df.size)  # Dataframe size
print(df.dtypes)  # Dataframe data type
print(df.T)  # Transpose Dataframe

print(df['Name'].iloc[1])  # Selecting a specific value in an specific column
print(df.iloc[1])

# ploting a dataframe
df['Age'].plot()
plt.show()
df.hist()
plt.show()

df['Height'].apply(np.sin)  # Apply function to apply a function to a dataframe
df['Height'].apply(lambda x: x * 100)  # Lambda function apply function to specific column or row

for key, value in df['Age'].iteritems():  # Iterating over dataframe
    print("{}: {}".format(key, value))


df.sort_values(by=['Name', 'Age'], inplace=True)  # Dataframe Sorting

####################
# Merging Dataframes


names = {
    'SSN': [2, 5, 7, 8],
    'Name': ['Anna', 'Bob', 'John', 'Mike']
}

ages = {
    'SSN': [1, 2, 3, 5],
    'Age': [28, 34, 45, 62]
}

df1 = pd.DataFrame(names)
df2 = pd.DataFrame(ages)

df = pd.merge(df1, df2, on='SSN', how='outer')  # Outer = All
                                                # Left = Priority on First dataframe
                                                # Right = Priority on Secound dataframe
                                                # Inner = only rows/columns were all information overlapped
df.set_index('SSN', inplace = True)

print(df)


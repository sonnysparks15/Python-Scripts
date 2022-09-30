###################################################
# Python For Data Science Lab 04
# Edwin (Sonny) Sparks
# September 15, 2022
###################################################

import math
import sys
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


def myFind(X, Y):
    listIndex = X
    i = 0
    while i < len(X):
        if X[i] == Y:
            listIndex.append(i)
        i = i + 1
    return listIndex


numbers = [9, -3, 7, 2, 1, 2, 9, 9, 8, 2, 0, 0, 9, 2]
myNum = input("Please enter a number to find: \n")
res = myFind(numbers, int(myNum))
print(res)

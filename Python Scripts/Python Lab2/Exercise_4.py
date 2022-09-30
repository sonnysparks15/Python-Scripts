###################################################
# Python For Data Science Lab 02
# Edwin (Sonny) Sparks
# September 1, 2022
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


def upperCaseCharacters(A):
    i = 0
    count = -1
    while i < len(A):
        if ord(A[i]) < 91:
            print(A[i])
            count = count + 1
        i = i + 1

    return count


myStr = input("Please enter a String: ")
Arr = list(myStr)
Count = upperCaseCharacters(Arr)
print("The number of capital letters is:", Count)


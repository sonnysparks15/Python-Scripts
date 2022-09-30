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


def myMinimum(*args):
    return min(*args)


i = input("Enter first number: ")  # Always a str
ii = input("Enter second number: ")  # Always a str
iii = input("Enter third number: ")  # Always a str
X1 = int(i)
X2 = int(ii)
X3 = int(iii)

Ans = myMinimum(X1, X2, X3)
print("The smallest value is:", Ans)





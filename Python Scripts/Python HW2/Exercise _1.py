###################################################
# Python For Data Science Homework 02
# Edwin (Sonny) Sparks
# September 4, 2022
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


def newtonSqrt(x):
    res = x
    prec = 0.00000001
    while abs(x - res * res) > prec:
        res = (res + x / res) / 2

    return res


X = input("Please enter a value to find square root of: ")
print("The square root of", X, "is:", newtonSqrt(int(X)))

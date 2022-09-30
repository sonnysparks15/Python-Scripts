###################################################
# Python For Data Science Homework 05
# Edwin (Sonny) Sparks
# September 26, 2022
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
import functools
####################################################
def int_dataTypes(X):
    if type(X) == str:
        return False
    if type(X) == float:
        return False
    else:
        return True


li = [9, "Robot", 3.14, 8, "Vision"]
Ans = filter(int_dataTypes, li)
print("The result of the filter is:", list(Ans))

###################################################
# Python For Data Science Homework 04
# Edwin (Sonny) Sparks
# September 20, 2022
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
def myFilter2(X):
    if X == 5 or X == 3 or X == 7:
        return True
    if X % 2 == 0:
        return False
    if X % 3 == 0:
        return False
    if X % 5 == 0:
        return False
    if X % 7 == 0:
        return False
    if X % 9 == 0:
        return False
    else:
        return True


numbers = [23, 2, 9, 7, 14, 18, 3, 24, 16, 5, 8, 97]
Ans = filter(myFilter2, numbers)
Answer = list(Ans)
print("\nThe prime result is: ", Answer)



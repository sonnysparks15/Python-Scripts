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
def myFilter(String):
    res = String
    i = 0
    while i < len(String):
        if ord(String[i]) != 111 and ord(String[i]) != 97\
                and ord(String[i]) != 101 and ord(String[i]) != 105\
                and ord(String[i]) != 117:
            res[i] = "_"
        i = i + 1
    print("Did this before realizing had to use filter --")
    print("The result is: ", ''.join(res))


def myFilter2(X):
    letters = ['a', 'e', 'i', 'o', 'u']
    if X in letters:
        return True
    else:
        return False


str1 = "Computer Science"
Str1 = [char for char in str1]
myFilter(list(Str1))

Ans = filter(myFilter2, list(str1))
print("\nThe real result is: ", ''.join(Ans))

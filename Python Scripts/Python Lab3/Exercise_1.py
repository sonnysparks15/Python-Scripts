###################################################
# Python For Data Science Lab 03
# Edwin (Sonny) Sparks
# September 8, 2022
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


def myTopUpper(String):
    i = 0
    while i < len(String):
        if ord(String[i]) > 96:
            String[i] = chr(ord(String[i])-32)
        i = i + 1
    return String


myStr = input("Please enter a string: \n")
MyStr = [char for char in myStr]
Res = myTopUpper(MyStr)
print(''.join(Res))

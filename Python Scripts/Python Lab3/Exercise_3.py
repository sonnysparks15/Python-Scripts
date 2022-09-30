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


def count(a):
    i = 0
    C = 0
    while i < len(tu1):
        if tu1[i] == int(a):
            C = C + 1
        i = i + 1
    return C


def index(b):
    ii = 0
    II = 0
    while ii < len(tu1):
        if tu1[ii] == int(b):
            II = ii
        ii = ii + 1
    return II


tu1 = [9, 3, 0, -4, 8, 7, 10, -1, 5]
A = input("Please enter a number to count in the tuple:")
Count = count(int(A))
Index = index(int(A))
print("The number of times your element occurred is:", Count)
print("The element occurred at indexes:", Index)


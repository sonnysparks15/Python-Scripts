###################################################
# Python For Data Science Lab 02
# Edwin (Sonny) Sparks
# September 1, 2022
###################################################

import math
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


def myFactorialWithForLoop(Num):
    factorial = 1
    for i in range(1, Num+1):
        factorial = factorial * i
    return factorial


i = 1
E = 1
while i <= 10:
    E = E + 1/myFactorialWithForLoop(i)
    i = i + 1

print("The Approximate of e is:", E)
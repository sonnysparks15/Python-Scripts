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


def myTopUpper(String):
    i = 0
    while i < len(String):
        if ord(String[i]) > 96:
            x = ord(String[i])-32
            print(chr(x), "\t")
        i = i + 1


myStr = input("Please enter a string: \n")
print("The lowercase value that are uppercase now are:\n")
myTopUpper(list(myStr))
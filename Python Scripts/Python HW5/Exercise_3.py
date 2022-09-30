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

opt = input("Please enter choice between (a) Fahrenheit->Celsius or (b) Celsius->Fahrenheit: (a or b)\n")
temp = input("Please enter temperature to convert:\n")
Conversion = lambda x, y: (float(temp) - 32) * (5/9) if opt == "a" else (float(y) * (9/5)) + 32
if opt == "a":
    print("The conversion of", temp, "Fahrenheit to Celsius is:", Conversion(opt, temp))
if opt == "b":
    print("The conversion of", temp, "Celsius to Fahrenheit is:", Conversion(opt, temp))



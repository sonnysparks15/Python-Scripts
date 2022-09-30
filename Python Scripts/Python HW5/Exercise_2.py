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
####################################################

opt = input("Please enter choice between (a) Miles->Kilometers or (b) Kilometers->Miles: (a or b)\n")
dist = input("Please enter distance to convert:\n")
Conversion = lambda x, y: float(y) * 1.609 if opt == "a" else float(y) * 0.621371
if opt == "a":
    print("The conversion of", dist, "miles to Kilometers is:", Conversion(opt, dist))
if opt == "b":
    print("The conversion of", dist, "Kilometers to Miles is:", Conversion(opt, dist))


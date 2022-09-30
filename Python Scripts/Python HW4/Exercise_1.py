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

X = input("Please enter a value to find the square root of:\n")
Root = lambda x: x**(1/2)
print("The square root is:", Root(float(X)))

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


li = [9, 3, 0, -4, 8, 7, 10, -1, 5]
print(li)
a = input("Please enter a start from the following list:"); A = int(a)
b = input("Please enter a stop from the following list:"); B = int(b)
c = input("Please enter a step:"); C = int(c)
print("The list in those parameters is:", li[A:B:C])

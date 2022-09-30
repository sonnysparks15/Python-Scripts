###################################################
# Python For Data Science Lab 05
# Edwin (Sonny) Sparks
# September 22, 2022
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

li = [10, "Hi", 20, "Hello", 30, "World", 40]
res = map(lambda x: x * 2 if type(x) == int else x, li)
print("The result is: ", list(res))

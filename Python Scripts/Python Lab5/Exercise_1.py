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

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
res = map(lambda x, y: x + y, tup1, tup2)
print("The Addition of Tup1 and Tup2 is: ", tuple(res))


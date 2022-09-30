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

myList = [3, 9.45, "Robotics", 8, 1]
print("The result is: ", ' '.join(list(map(lambda x: x.upper(), filter(lambda x: type(x) == str, myList)))))

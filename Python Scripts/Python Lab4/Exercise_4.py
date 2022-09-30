###################################################
# Python For Data Science Lab 04
# Edwin (Sonny) Sparks
# September 15, 2022
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


def greetingFunction(name, greet):
    res = lambda x, y: x + " " + y
    print(res(greet, name))


str1 = input("Please enter your name: \n")
str2 = input("Please enter a greeting: \n")
print(str2 + " " + str1)
greetingFunction(str1, str2)

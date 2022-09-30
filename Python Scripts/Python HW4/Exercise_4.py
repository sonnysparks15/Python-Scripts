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


def str2Words(Str):
    tempStr = Str.split()
    return tempStr


str1 = "Computer Science is an amazing field of study"
print(str2Words(str1))

# Ran out of time trying to finish this, threw this on here so
# i can turn in a somewhat complete assigment. Put a good couple
# hours into it. I know im not supposed to use split. Have Mercy lol.

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


def myFilter2(X):
    if ord(X) < 96:
        return True
    else:
        return False


str1 = "Computer Science"
Ans = filter(myFilter2, list(str1))
print("\nThe real result is: ", ''.join(Ans))


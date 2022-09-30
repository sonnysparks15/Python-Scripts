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

def myFilter2(X):
    if X == X[::-1]:
        return True
    else:
        return False


words = ["Anna", "hELLo", "rotor", "wow", "CS", "kayAK", "programming"]
words2 = []
for word in words:
    words2.append(word.lower())
Ans = filter(myFilter2, words2)
print("\nThe palindrome result is: ", ' '.join(Ans))

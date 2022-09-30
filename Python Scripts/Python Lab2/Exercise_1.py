###################################################
# Python For Data Science Lab 02
# Edwin (Sonny) Sparks
# September 1, 2022
###################################################

import math
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
import myFunctions
####################################################


while True:
    i = input("Enter first number: ")  # Always a str
    ii = input("Enter second number: ")  # Always a str
    X1 = float(i)
    X2 = float(ii)

    Op = input("Choose an operation to preform [+, -, *, /]: ")

    if Op == "+":
        ans = myFunctions.addition(X1, X2)
        print("\nThe addition of", X1, "and", X2, "is :", ans, "\n")
    elif Op == "-":
        ans = myFunctions.subtraction(X1, X2)
        print("\nThe subtraction of", X1, "and", X2, "is :", ans, "\n")
    elif Op == "*":
        ans = myFunctions.multiplication(X1, X2)
        print("\nThe multiplication of", X1, "and", X2, "is :", ans, "\n")
    elif Op == "/":
        ans = myFunctions.division(X1, X2)
        print("\nThe division of", X1, "and", X2, "is :", ans, "\n")
    else:
        break
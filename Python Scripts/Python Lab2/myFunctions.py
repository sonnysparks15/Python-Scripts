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
####################################################


def addition(number1, number2):
    X = number1 + number2
    return X


def subtraction(number1, number2):
    X = number1 - number2
    return X


def multiplication(number1, number2):
    X = number1 * number2
    return X


def division(number1, number2):
    X = number1 / number2
    return X



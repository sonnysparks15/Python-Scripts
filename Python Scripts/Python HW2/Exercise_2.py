###################################################
# Python For Data Science Homework 02
# Edwin (Sonny) Sparks
# September 4, 2022
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


def myFind(String, Character):
    x = ord(Character)
    i = 0; count = 0
    while i < len(String):
        if ord(String[i]) == x:
            print("The index of your character is: String[", i, "]")
            count = count + 1
        i = i + 1
    return count


myStr = input("Please enter a string: \n")
myChar = input("Please enter a character to find: \n")
C = myFind(list(myStr), myChar)
print("Your character occurred", C, "times.")

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
####################################################

speed = input("Please enter speed of car (km/h):\n")
dist = input("Please enter distance from leading car (m):\n")
Time_Collision = lambda x, y: (int(y)/(1000*int(x)/3600))
print("The time to collision is:", Time_Collision(speed, dist), "sec")

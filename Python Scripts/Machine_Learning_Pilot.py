###################################################
# Machine Learning Pilot
# Edwin (Sonny) Sparks
# April 24, 2022
###################################################

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


# %%###################################################
# Machine Learning #
###############################
# %% Linear Regression #
time_studied = np.array([20, 50, 32, 65, 23, 43, 10, 5, 22, 35, 29, 5, 56]).reshape(-1, 1)
score = np.array([56, 83, 47, 93, 47, 82, 45, 23, 55, 67, 57, 4, 89]).reshape(-1, 1)
time_train, time_test, score_train, score_test = train_test_split(time_studied, score, test_size=0.3)

model = LinearRegression()
model.fit(time_train, score_train)
print(model.score(time_test, score_test))
print(model.predict(np.array([56]).reshape(-1, 1)))

plt.scatter(time_train, score_train)
plt.plot(np.linspace(0, 70, 100).reshape(-1, 1), model.predict(np.linspace(0, 70, 100).reshape(-1, 1)), 'r')
plt.ylim(0, 100)
plt.show()

# %% K-Nearest Neighbors #
data = load_breast_cancer()
print(data.feature_names)
print(data.target_names)

x_train, x_test, y_train, y_test = train_test_split(np.array(data.data), np.array(data.target), test_size=0.2)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(x_train, y_train)

print('K-Nearest Neighbors Accuracy :')
print(clf.score(x_test, y_test))

# %% Support Vector Machines #
data = load_breast_cancer()

x_train, x_test, y_train, y_test = train_test_split(np.array(data.data), np.array(data.target), test_size=0.2)

cclf = SVC(kernel='linear', C=3)
cclf.fit(x_train, y_train)

print('Support Vector Machine Accuracy :')
print(cclf.score(x_test, y_test))

# %% Decision Trees and Random Forest #

cccclf = RandomForestClassifier()
cccclf.fit(x_train, y_train)

print(f'SVC: {cclf.score(x_test, y_test)}')
print(f'KNN: {clf.score(x_test, y_test)}')
# print(f'DTC: {ccclf.score(x_test, y_test)}')
print(f'RFC: {cccclf.score(x_test, y_test)}')
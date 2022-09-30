###################################################
# Python Pilot
# Edwin (Sonny) Sparks
# March 27, 2022
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
####################################################

#Getting into pip and CondaSparks:
# Terminal > conda activate CondaSparks
# pip install....
# exit

####################################################
# Beginner Lessons #
###############################
# %% Variables #
# str "Hello"'World'
# int 10
# complex 10,5          #10+5i
# bool True False
print("Hello"'World!')
print("10" + "10")
print(10 + 10)
# type function - Returns variable type
print(type(10))
# Defining Variable
x = 10
y = "Hello"
whatever = True
# Type Calculation
x1 = "120"
x1 = int(x1)
print(x1 / 4)

################################
# %% Operators and User Input #
# Arithmetic (+ - * /)
print(8 / 4)
# Modulus %
print(10 % 3)
# Exponent **
print(2 ** 5)
# Floor Division //
print(10 // 3)
# Assignment Operators (= += -= *= /= %= **= //=)
xx = 10
xx += 10
print(xx)
# Comparison Operators (== != < > >= <=)
print(10 == 11)
print("Hello" == "Hi")
# Logical Operators (and or not)
print(not True)
# User Input
X = input("Enter number one: ")  # Always a str
Y = input("Enter number two: ")
X = int(X)
Y = int(Y)
print(X + Y)

#################################
# %% If Statements and Conditions #
if X < Y:
    print("X is less than Y!")
elif X > Y:
    print("X is greater than Y!")
    if X > 100:
        print("X is greater than 100!")
else:
    print("X is equal to Y!")

#################################
# %% While and For Loops #
o = 0
while o < 10:
    o += 1
    print(o)
while True:
    print("Something")
    break
for XX in range(1, 11):  # Continue skips the bottom of the loop
    XX += 1
    if XX == 8:
        continue
    print(XX)
if X == 25:  # Fills a gap to run code intermittently
    pass

###################################
# %% Sequences and Collections #
mylist = [10, 20, 30, 8.19, True]
print(mylist[0])  # Displays 10
print(mylist[:3])  # Displays 10, 20, 30
print(mylist[-1])  # Displays True
for r in mylist:
    print(r)
s = [1, 2, 3]
d = [4, 5, 6]
S = s + d
# Functions of List
len(mylist)  # Length of List
max(mylist)  # Max value of List (can't have str or bool)
min(mylist)  # Min value of List (can't have str or bool)
# List Methods
# mylist.append(False)  # Adds a value to end of list
# mylist.insert(2, 8.99)  # Adds a value at specific element and shifts all elements down
# mylist.remove(True)  # Removes True from list anywhere it is
# mylist.pop(0)  # Removes element at specific element place
# mylist.index("20")  # Displays 1, elemental place that 20 is at
# mylist.sort()  # Sorts list smallest to the biggest
# Tuple's - Like list but can't be changed
mytuple = (1, 2, 3)
# Dictionary - Has Key values
person = {'name': 'Mark', 'age': 25, 'gender': 'male'}
print(person['age'])  # Displays 25
person['new key'] = 67
# Dictionary Methods
print(person.items())  # Displays list of tuples of pairs so 'name':'Mark'
print(person.keys())  # Displays all the keys of the dictionary
print(person.values())  # Displays all the Values of the Dictionary
# Membership operators (in not in)
print(3 in mylist)  # Displays False 3 is not in mylist
# Identity operators (is, is not)
if type(x) is int:
    print("x is int")
else:
    print("x is not int")


##################################
# %% Functions #
def add(m=0, n=0):  # Default Values 0 if not entered
    print(m + n)


def mysum(*numbers):  # Variable amount of parameters
    result = 0
    for number in numbers:
        result += number
        return result


print(mysum(10, 20, 30, 40, 50))

##################################
# %% File Operations #
# file = open('myfile.txt', 'w' 'r' 'a')  # w for writing a file, r for reading and a for appending




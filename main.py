# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
    dataset = pd.read_csv('/Users/gary/Desktop/Projects/DataScience/Data.csv')

    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    print (x)
    print (y)
    immputer = SimpleImputer(missing_values=np.nan,strategy='mean')
    immputer.fit(x[:, 1:3])
    X = immputer.transform(x[:, 1:3])

    print (X)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

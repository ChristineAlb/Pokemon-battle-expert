""".

Gotta catch em all

"""
import os
import xlrd
import numpy as np
from matplotlib.pyplot import figure, plot, title, legend, xlabel, ylabel, show

# ------ Import course toolbox ------
# from tmgsimple import TmgSimple

# ------ Import data ----- #
dir = os.getcwd()
doc = dir + '/battle-expert/datasheet/Concrete_Data.xls'
concreteList = xlrd.open_workbook(doc).sheet_by_index(0)

# Extract attribute names (1st row, column 1 to 9)
attributeNames = concreteList.row_values(0, 0, len(concreteList.row_values(0)))

# Preallocate memory, then extract excel data to matrix X
X = np.mat(np.empty(
    (len(concreteList.col_values(0)) - 1, len(concreteList.row_values(0)))))
for i, col_id in enumerate(range(0, 9)):
    X[:, i] = np.mat(concreteList.col_values(
        col_id, 1, len(concreteList.col_values(0)))).T

# Summary statistics of the datasheet
summary = X.head
summary = summary.transpose()
print(X.head)

# Compute values of N and M.
N = len(np.empty((len(concreteList.col_values(0)) - 1)))
M = len(concreteList.row_values(0))


'''
# Data attributes to be plotted
i = 0
j = 1

f = figure()
title('NanoNose data')

for c in range(C):
    # select indices belonging to class c:
    class_mask = y.A.ravel() == c
    plot(X[class_mask, i], X[class_mask, j], 'o')

legend(classNames)
xlabel(attributeNames[i])
ylabel(attributeNames[j])
'''

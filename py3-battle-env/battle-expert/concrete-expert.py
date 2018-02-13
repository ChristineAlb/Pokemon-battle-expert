""".

Gotta catch em all

"""
import os
import xlrd
import numpy as np

# ------ Import course toolbox ------
# from tmgsimple import TmgSimple

# ------ Import data ----- #
dir = os.getcwd()
doc = dir + '/battle-expert/datasheet/Concrete_Data.xls'
concreteList = xlrd.open_workbook(doc).sheet_by_index(0)

# Extract attribute names (1st row, column 1 to 9)
attributeNames = concreteList.row_values(0, 0, 9)

# Preallocate memory, then extract excel data to matrix X
X = np.mat(np.empty((1030, 9)))
for i, col_id in enumerate(range(0, 9)):
    X[:, i] = np.mat(concreteList.col_values(col_id, 1, 1031)).T

print(X)

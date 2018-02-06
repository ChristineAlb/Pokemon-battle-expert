import numpy as np
import pandas as pd
import os
import xlrd

from matplotlib.pyplot import figure, plot, title, legend, xlabel, ylabel, show
from scipy.linalg import svd

# ------ Import data ----- #
dir = os.path.dirname(__file__)
doc = os.path.join(dir, '../battle-expert/Toolbox_Python/Data/nanonose.xls')
doc = xlrd.open_workbook(doc).sheet_by_index(0)

# Extract attribute names (1st row, column 4 to 12)
attributeNames = doc.row_values(0, 3, 11)

# Extract class names to python list,
# then encode with integers (dict)
classLabels = doc.col_values(0, 2, 92)
classNames = sorted(set(classLabels))
classDict = dict(zip(classNames, range(5)))

# Extract vector y, convert to np matrix and transpose
y = np.mat([classDict[value] for value in classLabels]).T

# Preallocate memory, then extract excel data to matrix X
X = np.mat(np.empty((90, 8)))
for i, col_id in enumerate(range(3, 11)):
    X[:, i] = np.mat(doc.col_values(col_id, 2, 92)).T

# Compute values of N, M and C.
N = len(y)
M = len(attributeNames)
C = len(classNames)

# Data attributes to be plotted
i = 0
j = 1

##
# Make a simple plot of the i'th attribute against the j'th attribute
# Notice that X is of matrix type (but it will also work with a np array)
# X = np.array(X) #Try to uncomment this line
# plot(X[:, i], X[:, j], 'o')

# %%
# Make another more fancy plot that includes legend, class labels,
# attribute names, and a title.
f = figure()
title('NanoNose data')

for c in range(C):
    # select indices belonging to class c:
    class_mask = y.A.ravel() == c
    plot(X[class_mask, i], X[class_mask, j], 'o')

legend(classNames)
xlabel(attributeNames[i])
ylabel(attributeNames[j])

# Output result to screen
# show()
# Subtract mean value from data
Y = X - np.ones((N, 1))*X.mean(0)

# PCA by computing SVD of Y
U, S, V = svd(Y, full_matrices=False)

# Compute variance explained by principal components
rho = (S*S) / (S*S).sum()

# Plot variance explained
figure()
plot(range(1, len(rho)+1), rho, 'o-')
title('Variance explained by principal components')
xlabel('Principal component')
ylabel('Variance explained')
show()

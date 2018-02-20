""".

Gotta catch em all

"""
import os
# import xlrd
import numpy as np
import pandas as pd
from matplotlib.pyplot import figure, plot, title, legend, xlabel, ylabel, show
from scipy.linalg import svd

# ------ Import course toolbox ------
# from tmgsimple import TmgSimple

# ------ Import data ----- #
dir = os.getcwd()
doc = dir + '/battle-expert/datasheet/Concrete_Data.xls'
concreteList = pd.read_excel(doc)
concreteList.columns = [
    'Cement', 'Slag', 'Ash', 'Water', 'Superplasticiziser', 'Coarse Aggregate',
    'Fine Aggregate', 'Age', 'Strenght']

# Extract attribute names (1st row, column 1 to 9)
attributeNames = concreteList.head(0)

# Summary statistics of the compressive strenght
concreteStrength = concreteList['Strenght']
concreteStrength.describe()

# Calculate quantiles
concreteStrengthQuantiles = concreteStrength.quantile([.25, .5, .75])
concreteStrengthQuantiles

# Create Strenght catagory column based on conditions
conditions = [
    (concreteList['Strenght'] < concreteStrengthQuantiles.iloc[0]),
    (concreteList['Strenght'] > concreteStrengthQuantiles.iloc[2])]
choices = ['Low', 'High']
concreteList['Strenght Catagory'] = np.select(
    conditions, choices, default='Medium')

# Summary of the new catagory
concreteList['Strenght Catagory'].value_counts()

# Extract class names to python list,
# then encode with integers (dict)
classLabels = concreteList['Strenght Catagory']
classNames = sorted(set(classLabels))
classDict = dict(zip(classNames, range(5)))

# Compute values of N and M.
N = concreteList.shape[0]
M = concreteList.shape[1]
C = len(classNames)

# Extract vector y, convert to np matrix and transpose
y = np.mat([classDict[value] for value in classLabels]).T
X = np.array(concreteList.iloc[:, 0:-2])

# Data attributes to be plotted
i = 1
j = 6

# attribute names, and a title.
f = figure()
title('NanoNose data')

for c in range(C):
    # select indices belonging to class c:
    class_mask = y.A.ravel() == c
    plot(X[class_mask, i], X[class_mask, j], 'o')
legend(classNames)

# Substract the mean
Y = X - np.ones((N, 1)) * X.mean(0)

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

""".

Gotta catch em all

"""
import os
# import xlrd
import numpy as np
import pandas as pd
from matplotlib.pyplot import figure, plot, title, legend, xlabel, ylabel, show

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

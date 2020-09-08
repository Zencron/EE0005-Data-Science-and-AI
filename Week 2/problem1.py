import numpy as np
import pandas as pd

trainData = pd.read_csv('train.csv')
print(trainData.head(22))
print("Data type : ", type(trainData))
print("Data dims : ", trainData.shape)
print(trainData.info()) #prints a list of all columns, number of non-null values in each column, and datatype of values in the column. Also shows a count of each datatype
print(trainData.describe()) #prints statistics for each column (count, mean, mix, max, etc.)
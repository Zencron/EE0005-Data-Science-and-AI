import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

train_data = pd.read_csv('train.csv',)
# print(train_data.head())
# print("Data type : ", type(train_data))
# print("Data dims : ", train_data.shape)
# print(train_data.info())


numeric_data = train_data.select_dtypes(include = np.int64)
numeric_data = numeric_data.drop(columns = ['MSSubClass' , 'OverallQual' , 'OverallCond'])
print(numeric_data.head())

print(numeric_data['SalePrice'].describe())
print(numeric_data['LotArea'].describe())

sb.jointplot(x = numeric_data['SalePrice'], y = numeric_data['LotArea'], height = 8)
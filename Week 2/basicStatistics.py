import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
sb.set()

pkmndata = pd.read_csv('pokemonData.csv')
# print(pkmndata.head())

# print("Data type : ", type(pkmndata))
# print("Data dims : ", pkmndata.shape)
# print(pkmndata.dtypes)

hp = pd.DataFrame(pkmndata['HP'])
print("Data type : ", type(hp))
print("Data dims : ", hp.size)
hp.head()
hp.describe()
f, axes = plt.subplots(1, 1, figsize=(24, 4))
sb.boxplot(hp, orient = "h")
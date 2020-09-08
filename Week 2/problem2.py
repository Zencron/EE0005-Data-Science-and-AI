import numpy as np
import pandas as pd

html_data = pd.read_html('https://en.wikipedia.org/wiki/2016_Summer_Olympics_medal_table')
print("Data type : ", type(html_data))
print("HTML tables : ", len(html_data))

medal_data = html_data[1]
top20 = medal_data.head(20)
print(top20.head(33))
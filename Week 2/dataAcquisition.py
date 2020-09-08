import numpy as numpy
import pandas as pandas

csv_data = pandas.read_csv('somedata.csv', header = None)
print(csv_data.head())
print("Data type : ", type(csv_data))
print("Data dims : ", csv_data.shape)

txt_data = pandas.read_table('somedata.txt', sep = "\s+", header = None)
txt_data.head()
print("Data type : ", type(txt_data))
print("Data dims : ", txt_data.shape)

xls_data = pandas.read_excel('somedata.xlsx', sheet_name = 'Sheet1', header = None)
xls_data.head()
print("Data type : ", type(xls_data))
print("Data dims : ", xls_data.shape)

json_data = pandas.read_json('somedata.json')
json_data.head()
print("Data type : ", type(json_data))
print("Data dims : ", json_data.shape)

html_data = pandas.read_html('http://www.imdb.com/title/tt0441773/fullcredits/?ref_=tt_ov_st_sm')
print("Data type : ", type(html_data))
print("HTML tables : ", len(html_data))
print(html_data[2].head())
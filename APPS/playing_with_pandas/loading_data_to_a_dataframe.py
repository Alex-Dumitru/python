import pandas as p

# load data from csv file
#Load data from txt files separated by comma (same principle applies)
print('Data loaded from csv')
df1 = p.read_csv('supermarkets.csv')
#print(df1)
# automatically the header is True, so 1st row will become the header
#df1 = p.read_csv('supermarkets.csv',header=None)
# print(df1)
# the index (first column) is also set automatically, but you can change it with
print(df1.set_index("ID"))   # ATTENTION: if you elliminate the header, then you cannot set the index because the key 'ID' will not be found

# to get the shape of your df
print(df1.shape)

print("-"*100) # print a separator between tabels in output

# Load data from json
print('Data loaded from json')
df2 = p.read_json('supermarkets.json')
print(df2)

print("-"*100) # print a separator between tabels in output

# Load data from xlsx
# ATTENTION: package xlrd is a dependency for this, make sure you have it installed
print('Data loaded from xlsx')
df3 = p.read_excel('supermarkets.xlsx',sheet_name=0)
print(df3)

print("-"*100) # print a separator between tabels in output

# Load data from 'csv' files which have other separator

print('Data loaded from csv with other separator')
df4 = p.read_csv('supermarkets_semi-colons.txt', sep=';')
print(df4)

print("-"*100) # print a separator between tabels in output

# Load data from a website

print('Data loaded from a website')
df5 = p.read_csv('https://pythonhow.com/supermarkets.csv')
print(df5)

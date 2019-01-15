import pandas as p

df1 = p.read_csv('supermarkets.csv')
df1 = df1.set_index('Address')
print(df1)
# Slicing a dataframe (via label based indexing)  ! this is upper bound inclusive
# - first range is done on the index column, second range is done on the header row
if False:
    print(df1.loc['735 Dolores St':'332 Hill St','ID':'Country'])
# - accessing a cell
if False:
    df1 = df1.set_index('ID')
    print(df1.loc[3,'State'])
    print(df1.loc[:,'State'])
    print(list(df1.loc[:,'State']))


# Slicing a dataframe (via index based indexing) ! this is upper bound exclusive
if False:
    print(df1.iloc[1:3,1:4])

# Slicing a dataframe (via combined indexing)
if False:
    print(df1.ix[3,'Name'])  #returns 3rd row, with column name 'Name'
    print(df1.ix[3,3])



# Deleting a row/column. Signal row with 0, and column with 1
# Can be used separate, or together...they are methods of the same object
# deleting on-the-fly by default
if False:
    print(df1.drop('City',1))
    print(df1.drop('3666 21st St',0))
    print(df1.drop('City',1).drop('3666 21st St',0))
    print(df1.drop(df1.index[0:3],0))
    print(df1.drop(df1.columns[0:3],1))

if False:
    print(df1.index)   #df1.index returns a list for your index column
    print(df1.columns) #df1.columns returns a list for your header row



# Updating/Adding columns/rows
if False:
    if False:
        # with the following notation, we add new column df1['col_name']
        df1['Continent'] = ['North America']
        # this gives a ValueError: Length of values does not match length of index
        # because we are passing only one Element (data for 1st row) in the Continent column, but we already have 6 rows (df1.shape)
    df1['Continent'] = df1.shape[0]*['North America']
    # df1.shape returns a tuple in the format (rows, numbers)
    # df1.shape[0] returns the number of rows, and [1] will return number of columns
    # so we multiply it to the item that we want to insert, so that all rows of the new column are populated with the same value
    print(df1)

    df1['Continent'] = df1['Country'] + ', ' + df1['Continent']
    print(df1)

    # no direct way to add rows :(
    # we must transpose the table (columns -> rows and rows -> columns)
    df1_t = df1.T
    # now we can use the same syntax as before
    df1_t['My Address'] = ['My ID','My City','My State','My Country','My Shop',100,'My Continent']
    df1 = df1_t.T # now transpose back to original format and name
    print(df1)

    # same principle applies also for updating, but we must specify an existing value for row/column index

# Merging 2 DataFrames
if False:
    df1 = p.read_csv('supermarkets.csv')
    df2 = p.read_json('supermarkets.json')
    dm = p.merge(left=df1, right=df2, on='ID')

    print(dm)

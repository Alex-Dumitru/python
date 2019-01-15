import pandas as p
from geopy.geocoders import Nominatim # to use geocoders internet connection is needed, to return latitude and longitude on the given address


df1 = p.read_csv('supermarkets.csv')

nom = Nominatim(scheme='http')
if False:
    address = nom.geocode('3666 21st St, San Francisco, CA 94114')
    print(address.latitude,address.longitude)

#update the Address column, to have the address that we need to pass to the geocoder
df1['Address'] = df1['Address'] + ', ' + df1['City'] + ', ' + df1['State'] + ', ' + df1['Country']
#print(df1)

# in pandas, we don't need to iterate over all cells from a row or a column
# in has methods that allows us to apply a function to entire column/row

# create a new column to store the coordinates and apply the nom.geocode() function to all elements in the Address column with the .apply() function
# in this case, we don't use parenthesis for the nom.geocode, they will be supplied by the apply() function internally
df1['Coordinates'] = df1['Address'].apply(nom.geocode)
# this way, we insert entire Location object (returned by nom.geocode) in the table
if False:
    # we can access just the Coordinates column
    print(df1.Coordinates)                    #<- this way looks cleaner
    print(df1['Coordinates'])
    # or we can access an attribute of a single element in the table
    print(df1.Coordinates[0].latitude)        #<- this way looks cleaner
    print(df1['Coordinates'][0].latitude)
if True:
    # df1['Latitude'] = df1['Coordinates'].apply(lambda x: x.latitude)    # this returns an error, because we have in the table a None value (geolocation failed on some address)
    df1['Latitude'] = df1['Coordinates'].apply(lambda x: x.latitude if x is not None else None)  # if x is not None apply the .latitude method and write the return value, else write None in the cell
    # we apply the same princile for longitude
    df1['Longitude'] = df1['Coordinates'].apply(lambda x: x.longitude if x is not None else None)
    print(df1.Latitude)
    print(df1.Longitude)

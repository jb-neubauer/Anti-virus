dict = {"country" : ["Brazil", "Russia", "India", "China", "South Africa"], 
	"capital" : ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
	"area" : [8.516, 17.10, 3.286, 9.597, 1.221],
	"population" : [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd 
brics = pd.DataFrame(dict)
print(brics)

brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

cars = pd.read_csv('cars.csv')

print(cars)

#import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

#print out country column as pandas series
print(cars['cars_per_cap'])

# print out country column as pandas dataframe
print(cars[['cars_per_cap']])

# print out dataframe with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

# prints out first 4 observations
print(cars[0:4])

# prints out fifth, sixth, and seventh observations
print(cars[4:6])

# print out observation for A country
print(cars.iloc[2])

# prints out observation based on abbreviation
print(cars.loc[['AUS', 'EG']])



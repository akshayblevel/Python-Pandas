import pandas as pd

file_name = 'price.csv'

# Read the CSV file and load the data into a Series
with open(file_name, 'r') as file:
   items = file.readline().strip().split(',')
   prices = file.readline().strip().split(',')

itemPrices = pd.Series([int(price) for price in prices], index=items)

print(itemPrices)

'''
Pizza        100
Burger       200
Sandwitch    300
Fries        400
Colddrink    500
dtype: int64
'''
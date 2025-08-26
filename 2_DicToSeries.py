import pandas as pd

prices = {
         'Pizza':100,
         'Burger':200,
         'Sandwitch':300,
         'Fries':400,
         'Colddrink':500
}

series = pd.Series(prices)
print(series)

'''
Pizza        100
Burger       200
Sandwitch    300
Fries        400
Colddrink    500
dtype: int64
'''

prices['Sandwitch'] = 350
series = pd.Series(prices)
print(series)

'''
Pizza        100
Burger       200
Sandwitch    350
Fries        400
Colddrink    500
dtype: int64
'''

# .loc[] is used to access or modify values in a Series using the label (index name)
series.loc['Sandwitch'] = 360
print(series)

'''
Pizza        100
Burger       200
Sandwitch    360
Fries        400
Colddrink    500
dtype: int64
'''

# .iloc[] accesses data by integer position (like list indexing)
series.iloc[2] = 370
print(series)

'''
Pizza        100
Burger       200
Sandwitch    370
Fries        400
Colddrink    500
dtype: int64
'''
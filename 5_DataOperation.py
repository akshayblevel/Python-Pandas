import pandas as pd

# Creating the list
intArray = [14, 10, 81, 16, 11, 84]

# Creating a Pandas Series
series = pd.Series(intArray)

print(series)
# Output
'''
0    14
1    10
2    81
3    16
4    11
5    84
dtype: int64
'''

# Filtering values greater than 30
data1 = series[series > 30]

print(data1)
# Output
'''
2    81
5    84
dtype: int64
'''

# Check if elements are either 10 or 30
data2 = series.isin([10,30])

print(data2)
# Output
'''
0    False
1     True
2    False
3    False
4    False
5    False
dtype: bool
'''

# Get elements that are either 10 or 30
data3 = series[data2] # This uses the boolean mask data2 to filter values from series

print(data3)
# Output
'''
1    10
dtype: int64
'''

# Convert all values to strings
data4 = series.astype(str)

print(data4)
# Output
'''
0    14
1    10
2    81
3    16
4    11
5    84
dtype: object
'''

# Filter string values containing the character '4'
data5 = data4[data4.str.contains('4')]
print(data5)
# Output
'''
0    14
5    84
dtype: object
'''
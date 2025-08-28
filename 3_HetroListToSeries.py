import pandas as pd

hetroList = [14,[14,10,81],True,["Akshay","Patel"],45]

series = pd.Series(hetroList)

print(series)

'''
0                 14
1       [14, 10, 81]
2               True
3    [Akshay, Patel]
4                 45
dtype: object
'''
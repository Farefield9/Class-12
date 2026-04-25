import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = pd.Series([11,2,3,4,5,6,7,8,np.nan,10,10])
print(a)
print(a.sum())
print(a.mean())
print(a.min())
print(a.max())
print(a.mode())
print(a.median())
print(a.count())
print(a.sort_values(ascending = False))
print('1'==1)

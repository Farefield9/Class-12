import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = ['a','b','c','d']
b = pd.Series(a,index=[2,5,6,2])
print(b[2])
b.rename({2:1,6:0},axis = 0, inplace = True)
print(b)

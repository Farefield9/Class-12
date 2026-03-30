import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = pd.Series([5000,4000,800,2000], index = ['cpu','monito','spek','ups'])
print(a[a>1000])
a.rename(index = {'cpu':'c'}, inplace = True)
print(a)

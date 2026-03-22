import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = pd.DataFrame({'rn':[1,2,3,4,5,6],'name':['p','m','t','f','k','r'],'ut1':[24,18,20,22,15,20],'ut2':[24,17,22,20,20,15],'ut3':[20,19,18,24,18,22],'ut4':[22,22,24,20,22,24]})
print(a)
print(a.max())
print(a[a['rn']==4])
print(a.count())
print(a.columns)
print(min(a['ut2']))
a.drop([1,2], axis = 0, inplace = True)
print(a)
print(a[a['ut1']>18])

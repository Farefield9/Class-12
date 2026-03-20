import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = pd.DataFrame({'school':['p','j','g','m','b'],'totstu':[40,30,20,10,20],'top':[32,18,18,10,20],'1':[2,12,2,8,8]},
                 index = ['co1','co2','co3','co4','co5'])
print(a)
print(a.shape)
print(a[2:4])
print(a.loc['co2':'co4','top':"top"])
print(a['totstu']-a['1'])
a[:] = 0
print(a)
a.rename(index={'co1':1}, inplace = True)
print(a)

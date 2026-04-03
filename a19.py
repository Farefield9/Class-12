import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = pd.DataFrame({'course':['mba','bsc','bcom','mca','btech'], 'university':['ln','vm','jk','vm','ln'],
                  'loc':['mumbai','pune','chennai','pune','mumbai'],'fees':[55000,65000,45000,70000,100000]},
                 index = ['a','b','c','d','e'])
print(a.shape[1])
a.pop('course')
print(a)
a['nfees'] = a['fees']+1
print(a)
a.drop(a.index[4],inplace = True)
print(a)
print(a[(a['course']!='mba') | (a['course'] != 'bsc')])
print(a[(a['course']!='mba') & (a['course'] != 'bsc')])
print(a[(a['course']=='mba') | (a['course'] == 'bsc')])
print(a[(a['course']=='mba') & (a['course'] == 'bsc')])
a.insert(1,'age',[1,2,3,4,5])
print(a)
print(a[(a['fees']>60000) & (a['fees']<70000)])
b = a[a['fees']>60000]
print(b[['course','loc']])
print(a[['loc','course']].sum())
print(a[a['course']=='mba'].index)
a.loc['c']=0
print(a)
print(a.loc[['e','b'],['course','fees']])
print(a.max())
print(a.loc[:,'course':'loc'])
print(a[a['loc']=='pune'])
a.loc[5,'fees'] = 80000
print(a)
print(a[a['loc']=='pune'].sum())

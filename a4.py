import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
df = pd.DataFrame({'s':['s1','s2','s3','s4'],
                  'q1':[300,350,200,100],
                  'q2':[240,340,180,100],
                  'q3':[450,403,145,100],
                  'q4':[230,210,160,100]})
print(df[1:3])
df.drop([3,2],axis = 0,inplace = True)
print(df)
df['total']=df['q1']+df['q2']+df['q3']+df['q4']
print(df)
a = df.to_csv('d:\\Mannan\\1.csv')
print(a)

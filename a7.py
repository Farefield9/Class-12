import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = pd.DataFrame({'name':['n','h','d','h'],'price':[150,180,225,500]})
a['s p'] = [135,150,200,440]
a.loc[4] = ['t', 800,450]
del a['s p']
print(a)

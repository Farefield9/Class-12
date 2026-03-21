import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
S1=pd.Series([5,6,7,8,10],index=['v','w','x','y','z'])
l=[2,6,1,4,6]
S2=pd.Series(l,index=['z','y','a','w','v'])
print(S2.head(-2))

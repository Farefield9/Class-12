import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = ['r','v','s',"r"]
b = [8,6,4,2]
pl.bar(a,b)
pl.yticks(np.arange(0,10,0.5))
pl.grid(axis = 'y')
pl.show()

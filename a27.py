import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = [1,2,3,4]
b = [10,20,30,40]
c = [10,20,30,40]
d = np.arange(len(a))
pl.bar(d,b,width = 0.15)
pl.bar(d+0.15,c,width = 0.15)
pl.xticks([1,2,3,4])
pl.show()

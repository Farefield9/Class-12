import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = [10,20,20,40]
b = [20,30,25,30]
c = np.arange(1,5,1)
pl.bar(c,a,width = 0.25, label = 'a')
pl.bar(c+0.25,b,width = 0.25, label = 'b')
pl.legend()
pl.show()

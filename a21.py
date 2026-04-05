import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,11,12,13,14,15,16,17,18,19]
pl.hist(a,bins= 2)
pl.xticks([0,10,20])
pl.yticks([0,10,20])
pl.show()

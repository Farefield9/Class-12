import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
l = [1,4]
print(l*2)
pl.hist([1,2,11,12,21,22,23,24,25], bins = [0,10,20,30])
pl.yticks(range(1,6))
pl.show()
pl.bar(['a','b'],[10,20])
pl.yticks([0,10,20])
pl.show()

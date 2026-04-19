import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
eng = [56,78,90,34]
sci = [65,77,54,32]
maths = [45,67,43,41]
a = np.arange(4)
pl.bar(a,eng,width = 0.25)
pl.bar(a+0.25,sci,width = 0.25)
pl.title('Subject Analysis')
pl.xlabel('Marks')
pl.ylabel('Subjects')
pl.show()

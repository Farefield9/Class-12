import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
a = pd.Series([350,200,800,150], index = ['table','chaair','sofa','stool'])
print(a[a>250])
a.name = 'a'
print(a)
a.index.name = 'b'
print(a)

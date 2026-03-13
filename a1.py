import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
di = {'Corbett': 'Uttarakhand', 'Sariska':'Rajasthan', 'Kanha': 'MadhyaPradesh','Gir':'Gujarat'}
NP = pd.Series(di)
print(NP[1])

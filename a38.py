import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
dic = {"Model": ["Samurai", "Accord", "CR-V", "Nexon"],"Brand": ["Suzuki", "Honda", "Honda", "Tata"],"Make": [1993, 1997, 1997, 2021]}
car = pd.Series(dic)
print(car)

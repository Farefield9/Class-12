import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
nums=pd.Series([9,8,7,6,5],index=[1,2,3,4,5])
print(nums.head(4))
print(nums.loc[1:3],nums[1:3])
nums.loc[6] = 7
print(nums)

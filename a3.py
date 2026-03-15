import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
genre = pd.DataFrame({'type':['fiction','nonfiction','drama','poetry'],
                      'code':['f','nf','d','p']})
genre['numcopies']= [300,290,450,760]
genre.loc[4] = ['folk tales','ft',600]
genre.rename({'code':'bookcode'}, inplace = True, axis = 1)
print(genre)

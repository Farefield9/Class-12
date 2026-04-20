import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
x=[1,2,3,4,5]
y=[50,40,70,80,20]
y2=[80,20,20,50,60]
y3=[70,20,60,40,60]
y4=[80,20,20,50,10]
pl.plot(x,y,'g',label='Enfield',linewidth=5)
pl.plot(x,y2,'c',label='Honda',linewidth=5)
pl.plot(x,y3,'k',label='Yamaha',linewidth=5)
pl.plot(x,y4,'y',label='KTM',linewidth=5)
pl.title('bike details in line plot')
pl.ylabel('Distance in kms')
pl.xlabel('Days')
pl.legend()
pl.show()

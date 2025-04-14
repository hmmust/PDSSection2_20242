import pandas as pd
import numpy as np
df1 = pd.DataFrame([10,20,30,40])
print(df1)
df2 = pd.DataFrame([['Layan',20,'DSAI'],
                    ['Lana',19,'DSAI'],
                    ['Waleed',21,'CS'],
                    ['Amr',22,'SE']],
                   index=[20201,20202,20203,20204],
                   columns=['name','mark','major'])
print(df2)
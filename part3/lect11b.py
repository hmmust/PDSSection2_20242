import pandas as pd
import numpy as np
#dictionary of [list,ndarray, series]
df2 = pd.DataFrame({'name':['Layan','Lana','Waleed','Amr'],
                    'mark':[20,19,21,22],
                    'major':['DSAI','DSAI','CS','SE']},
                   index=[20201,20202,20203,20204])
print(df2)
df3 = pd.DataFrame({'name':np.array(['Layan','Lana','Waleed','Amr']),
                    'mark':np.array([20,19,21,22],dtype=np.int32),
                    'major':np.array(['DSAI','DSAI','CS','SE'])},
                   index=[20201,20202,20203,20204])
print(df3)
df4 = pd.DataFrame({'name':pd.Series(['Layan','Lana','Waleed','Amr'],
                                     index=[20201,20202,20203,20204]),
                    'mark':pd.Series([20,19,21,22],dtype=np.float32,
                                     index=[20201,20202,20203,20204]),
                    'major':pd.Series(['DSAI','DSAI','CS'],
                                     index=[20204,20201,20202])},
                   index=[20201,20202,20203,20204])
print(df4)
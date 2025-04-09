import pandas as pd
import numpy as np
ser1 = pd.Series([22,23,24,26])
ser1 = pd.Series(np.array([22,23,24,26]),
                 index=[202301,202302,202303,202304])
print(ser1)
print(ser1[202303])
ser2 = pd.Series(np.array([20,19,18,30]),
                 index=['layan','lana','abed','raghad'])
print(ser2)
print(ser2['raghad'])
print(ser2[-2:])
print(ser1[ser1>22])
print(ser1.where(ser1>22))
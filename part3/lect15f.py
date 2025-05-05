import pandas as pd
import numpy as np
import datetime


print(pd.date_range('2025/5/5 9:00',periods=12, freq='15min'))
print(pd.date_range('2025/5/5 8:00',periods=5, freq='90min'))
print(pd.date_range(datetime.datetime(2025,5,5,8,0),
                    periods=5, freq=pd.Timedelta(minutes=90)))
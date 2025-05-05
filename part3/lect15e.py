import pandas as pd
import numpy as np
import datetime
print(datetime.datetime.now())
today= datetime.datetime.today()
layan_birthdate= datetime.datetime(2004,7,25)
print(type(today-layan_birthdate)) #timedelta 
dt_lectures = pd.Timedelta('1 hour 30 minute')
dt_lectures = pd.Timedelta(hours=1, minutes=30)
print(dt_lectures)
print(today+dt_lectures)
print(today-dt_lectures)
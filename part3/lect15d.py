import pandas as pd
import numpy as np

import datetime
print(datetime.datetime.now())
today= datetime.datetime.today()
print(type(today))
print(today.month)
layan_birthdate= datetime.datetime(2004,7,25)
print(layan_birthdate)
print(today-layan_birthdate)
print(type(today-layan_birthdate))

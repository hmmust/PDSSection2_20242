import time
import pandas as pd
import numpy as np

students = pd.read_csv("./part3/students.csv",chunksize=3)
for data in students:
    print(data)

import pandas as pd
import numpy as np
from matplotlib import pyplot
students_df = pd.read_csv('./part3/students.csv',
                          names=['id','fullname','major','age',
                                 'accept_year','GPA'],header=0,
                          dtype={'GPA':np.float32,
                                 'age':np.int16})
print(students_df.major.value_counts().plot.bar())
pyplot.show()
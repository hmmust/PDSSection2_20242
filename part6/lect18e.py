import multiprocessing
import time
import pandas as pd
import numpy as np
def read_csv(students_df):
    students_df.Year.replace({np.nan:2015},inplace=True)
    students_df.Major.replace({"DSS":"DS"," SE":"SE"},inplace=True)
    students_df.Age=students_df.Age.astype(np.int16)
    return students_df
if __name__== "__main__":
    pool = multiprocessing.Pool(processes=4)
    students = pd.read_csv('./part3/students.csv',chunksize=3)
    all_students = []
    for data in students:
        new_data = pool.apply_async(read_csv,args=(data,))
        all_students.append(new_data.get())
    pool.close()
    pool.join()
    all_students = pd.concat(all_students,axis=0,ignore_index=True)
    print(all_students)

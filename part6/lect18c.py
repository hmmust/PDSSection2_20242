import multiprocessing
import time
import pandas as pd
import numpy as np
def read_csv(filepath):
    print("Reading {}".format(filepath))
    time.sleep(1)
    students_df = pd.read_csv(filepath)
    students_df.Year.replace({np.nan:2015},inplace=True)
    students_df.Major.replace({"DSS":"DS"," SE":"SE"},inplace=True)
    #students_df.Year=students_df.Year.astype(np.int16)
    students_df.Age=students_df.Age.astype(np.int16)
    return students_df
if __name__== "__main__":
    pool = multiprocessing.Pool(processes=2)
    part1 = pool.apply_async(read_csv,args=('./part6/students1.csv',))
    part2 = pool.apply_async(read_csv,args=('./part6/students2.csv',))
    pool.close()
    pool.join()
    all_students = pd.concat([part1.get(),part2.get()],axis=0,ignore_index=True)
    print(all_students)

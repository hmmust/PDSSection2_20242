import multiprocessing
import time
#print(multiprocessing.cpu_count())
def count_numbers(n):
    sum =0
    for i in range(n):
        sum += i
        print(n,sum)
        time.sleep(1) 
    return sum  
if __name__== "__main__":
    pool = multiprocessing.Pool(processes=2)
    sum1 = pool.apply_async(count_numbers,args=(5,))
    sum2 = pool.apply_async(count_numbers,args=(10,))
    pool.close()
    pool.join()
    print("Done",sum1.get(),sum2.get())

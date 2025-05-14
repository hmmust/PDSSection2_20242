import multiprocessing
import time
#print(multiprocessing.cpu_count())

def count_numbers(n):
    for i in range(n):
        print(n,i)
        time.sleep(1)
        
if __name__== "__main__":
    process1 = multiprocessing.Process(target=count_numbers, args=(5,))
    process2 = multiprocessing.Process(target=count_numbers, args=(10,))
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    print("Done E")

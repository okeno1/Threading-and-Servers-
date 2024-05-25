'''
### Recall on threading ### Without ThreadPoolExceptor

import time
import threading

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print('Done Sleeping...')
    

threads=[]

for _ in range(100):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')

'''
###############################################################
#######################MultiProcessing#########################
#import multiprocessing
import concurrent.futures
import time

def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        '''
        f1 = executor.submit(do_something, 1)
        f2 = executor.submit(do_something, 1)
        
        print(f1.result())
        print(f2.result())
        '''
        secs = [5,4,3,2,1]
        results = [executor.submit(do_something,sec) for sec in secs]
        
        for f in concurrent.futures.as_completed(results):
            print(f.result())
        

    # Uncomment the block below to use multiprocessing manually
    '''
    processes = []
    
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)
        
    for process in processes:
        process.join()
    '''

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')

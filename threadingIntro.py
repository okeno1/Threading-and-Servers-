import concurrent.futures
#import threading
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    '''
    results = [executor.submit(do_something,sec) for sec in secs]
    
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    '''
    #Using map instead of list comprehension
    results = executor.map(do_something, secs)
    
    for result in results:
        print(result)

'''
threads = []
    
for _ in range(10):
    t = t1 = threading.Thread(target=do_something,args=[1.5])
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()

'''

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
#Multithreading and multiprocessing
import time
import threading
from functools import wraps
import multiprocessing
from multiprocessing import Process

def time_taken(name):
    def decorator(function):
        @wraps(function)
        def wrapper():
            start = time.time()
            function()
            end = time.time()
            print(f"time taken by {name}: {end - start:.2f} Seconds.")
        return wrapper
    return decorator
        
# def tuin():
#     for i in range(2):
#         print("Tuin")
#         time.sleep(1)
        
# def jina():
#     for i in range(2):
#         print("Jina")
#         time.sleep(1)

# def sriya():
#     for i in range(2):
#         print("Sriya")
#         time.sleep(1)
        
# @time_taken("multithreading")
# def task_with_multithreading():

#     sriya_thread = threading.Thread(target=sriya)
#     jina_thread = threading.Thread(target=jina)
#     tuin_thread = threading.Thread(target=tuin)

#     sriya_thread.start()
#     jina_thread.start()
#     tuin_thread.start()

#     sriya_thread.join()
#     jina_thread.join()
#     tuin_thread.join()
    
# @time_taken("sequential")
# def task_without_mulitithreading():
#     sriya()
#     jina()
#     tuin()
    
# @time_taken("multiprocessing")
# def task_with_multiprocessing():
#     Sriya = Process(target=sriya)
#     Jina = Process(target=jina)
#     Tuin = Process(target=tuin)
        
#     Sriya.start()
#     Jina.start()
#     Tuin.start()
        
#     Sriya.join()
#     Jina.join()
#     Tuin.join()

# if __name__ == "__main__":
#     task_with_multithreading()
#     task_without_mulitithreading()
#     task_with_multiprocessing()

def cpu_heavy_task():
    print(f"Starting CPU heavy task.")
    count = 0
    for i in range(10**10):
        count += i
    print("CPU heavy task completed.")
    print(f"The addition of 0 tp 10**10 is {count}.")
    
@time_taken("multithreading")
def multithreading_task():
    t1 = threading.Thread(target=cpu_heavy_task)
    t2 = threading.Thread(target=cpu_heavy_task)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
@time_taken("multiprocessing")
def multiprocessing_task():
    p1 = Process(target=cpu_heavy_task)
    p2 = Process(target=cpu_heavy_task)
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

if __name__ == "__main__":
    multithreading_task()
    multiprocessing_task()
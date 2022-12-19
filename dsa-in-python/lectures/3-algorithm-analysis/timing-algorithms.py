from time import time


def using_time_function():
    start_time = time() 
    end_time = time()
    elapsed = end_time - start_time
    print(elapsed)
import time
import concurrent.futures

def calc_square(numbers):
    print("calculate square numbers \n")
    for n in numbers:
        print('square:',n*n , '\n')
        time.sleep(1)
 

def calc_cube(numbers):
    print("calculate cube of numbers \n")
    for n in numbers:
        print('cube:',n*n*n , '\n')
        time.sleep(1)


arr = [2,3,8]

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

pool.submit(calc_square , arr) 
pool.submit(calc_cube , arr)

pool.shutdown(wait=True)

print("Main thread continuing to run")

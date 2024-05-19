import multiprocessing
import time
def squer (num):
    for n in num:
        print("squer:"+str(n*n))
        time.sleep(3)
def cup (num):
    for n in num:
        print("cup:"+str(n*n*n))
        time.sleep(3)
if __name__=="__main__":
    arr=[2,3,4]
    t=time.time()
    p1=multiprocessing.Process(target=squer ,args=(arr,))
    p2=multiprocessing.Process(target=cup,args=(arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("thes process done in",time.time()-t)
    
    

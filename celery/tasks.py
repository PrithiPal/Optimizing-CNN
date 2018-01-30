from celery import Celery
import threading
import time
import math
import numpy as np

app = Celery('tasks',broker='redis://:babaji@localhost:6379/0',backend='redis://:babaji@localhost:6379/0')

def generate_arr(thread_no, n, s,e) :
    l = threading.Lock()
    t1 = time.time()
    print('Thread {} : starting '.format(thread_no))

    l.acquire()

    #n = int(n)
    #new_n = int(math.pow(10,2*n))
    #arr = np.random.rand(new_n)
    #B[s:e] = arr[0:len(arr)-1]

    l.release()


    t2 = time.time() - time1
    print('Thread {} : ended [{} left]'.format(thread_no,threading.active_count()))

    return 1

class array_thread(threading.Thread) :
    def __init__(self,num,start,end,n) :
        threading.Thread.__init__(self)
        self.num = num
        self.b_start = start
        self.b_end = end
        self.arr_length = n

    def run(self) :
        generate_arr(self.num,self.arr_length,self.b_start,self.b_end)

@app.task
def add(x,y) :
    return x+y
@app.task
def subtract(x,y) :
    return x-y

@app.task
def create_random_arr(n,num_threads) :
    global time1
    time1 = time.time()

    #global B
    #N = int(math.pow(10,10))
    #B = np.zeros(N)


    ## dividing into 10 threads
    start_ind=0
    end_ind=-1

    for i in range(num_threads) :
        start_ind = end_ind+1
        end_ind = ((i+1)*int(math.pow(10,8)))-1
        #t = threading.Thread(target=generate_arr,args=(i,n_thread,start_ind,end_ind))
        print('Thread {} started'.format(i))
        t = array_thread(i,start_ind,end_ind,n)
        t.start()
        print('Thread {} completed'.format(i))

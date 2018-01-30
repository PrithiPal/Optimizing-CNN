import threading
import numpy as np
import time
import math





def generate_arr(thread_no, n, s,e) :
    l = threading.Lock()
    t1 = time.time()
    print('Thread {} : starting '.format(thread_no))

    ## critical region starts
    ##l.acquire()

    ## generate array
    n = int(n)
    new_n = int(math.pow(10,2*n))
    arr = np.random.rand(new_n)

    ## append to B array
    #print(B.shape)
    #print(arr.shape)
    B[s:e] = arr[0:len(arr)-1]

    ##l.release()
    t2 = time.time() - time1
    print('Thread {} : ended [{} left]'.format(thread_no,threading.active_count()))

    return 1

def main() :
    global time1
    time1 = time.time()
    n = 4
    global B
    N = int(math.pow(10,10))
    B = np.zeros(N)
    n_thread=n

    ## dividing into 10 threads
    start_ind=0
    end_ind=-1

    for i in range(100) :
        start_ind = end_ind+1
        end_ind = ((i+1)*int(math.pow(10,8)))-1
        t = threading.Thread(target=generate_arr,args=(i,n_thread,start_ind,end_ind))
        t.start()






if __name__ == '__main__' :
    main()

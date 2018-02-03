

import threading
import time
def func(a,b,num) :
    for i in range(a) :
        l = threading.Lock()
        print('Thread {} : before b = {}'.format(num, b))
        
        l.acquire()
        b = b+1
        l.release()
        print('Thread {} : after b = {}'.format(num, b))
    return


def main() :

    t1 = threading.Thread(target=func,args=(10,0,1))
    t2 = threading.Thread(target=func,args=(20,0,2))

    t1.start()
    t2.start()
    t2.join()

    return 1

if __name__ == '__main__' :
    main()

import threading
from threading import Event
import time


def thread1(e) :
    print('Thread 1 : starting')
    e.wait()
    print('Thread 1 : finishing')

def thread2(e) :
    print('Thread 2 : starting ')
    r=1
    while int(r)!=0  :
        r = input('Enter 0 to quit')
    e.set()
    print('Thread 2 : fishing')

def main() :


    e = Event()
    t1 = threading.Thread(target=thread1,args=(e,))
    t2 = threading.Thread(target=thread2,args=(e,))
    t1.start()
    t2.start()

if __name__ == '__main__' :
    main()

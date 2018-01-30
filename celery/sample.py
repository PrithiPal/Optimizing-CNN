import threading

def add(x,y) :
    return x+y

if __name__ == '__main__' :
    for i in range(1000) :
        t = threading.Thread(target=add,args=(4,3,))

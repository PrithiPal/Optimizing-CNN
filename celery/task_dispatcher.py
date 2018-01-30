from celery import Celery



app = Celery('tasks',broker='redis://:babaji@localhost:6379/0',backend='redis://:babaji@localhost:6379')

if __name__ == '__main__' :



    ARRAY_SIZE_FACTOR = 6 ## n
    NUM_THREADS = 5 ## num_threads
    result = app.send_task('tasks.create_random_arr',args=(ARRAY_SIZE_FACTOR,NUM_THREADS,))
    print('Initiating {} threads for array (10*{})'.format(NUM_THREADS,ARRAY_SIZE_FACTOR))

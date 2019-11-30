# Multi Processing  --- Done
# when to USe Threading when to Use MultiProcessor  --- Done
# With Statement -- use for reading/writing files sockets etc
# Request Module(RESTAPI)
# JSON PARSER
# DATABASE CONNECTIVITY
# OS MODULE
# SHELL COMMANDS MODULE
# Decorators - Getters, Setters, and Deleters
# Lambda MAP Filter Reduce Revision
# class instance abstract class
# What are metaclasses in Python?
# Does Python have a ternary conditional operator?

import multiprocessing
from time import sleep
from multiprocessing import Pool
import time

'''
def print_cube(num):
    print("Cube: {}".format(num * num * num))


def print_square(num):
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print("Done!")
print('---------------------------------------------------------------------------------------------------------------')

'''
'''
class A(object):
    def __init__(self, *args, **kwargs):
        # do other stuff
        pass

    def do_something(self, i):
        sleep(0.2)
        print('%s * %s = %s' % (i, i, i*i))

    def run1(self):
        processes = []

        for i in range(1000):
            p = multiprocessing.Process(target=self.do_something, args=(i,))
            p.start()
            processes.append(p)

        [x.start() for x in processes]


if __name__ == '__main__':
    a = A()
    a.run1()
'''

print('---------------------------------------------------------------------------------------------------------------')


def square(para):
    s = 0
    for i in range(para):
        s += i * i
    return s


if __name__ == '__main__':  # It has to be there to guard subprocess from creating infinite process
    para = range(5)
    p = Pool()  #Creating Object of pool class.
    ''' Pool can be used for parallel execution of a function across multiple input values, distributing the input data across processes (data parallelism).'''
    result = p.map(square, para) #calling object.method via p.map()
    print(result)
    p.close()  # This indicates that I am not going to create more worker for the pool
    p.join() # Wait for worker Process to terminate

# https://www.youtube.com/playlist?list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN
'''
In computer science, a lock or mutex (from mutual exclusion) is a 
synchronization mechanism for enforcing limits on access to a resource in an environment where there are many threads of execution
Multi Threading:
------------------
1.  It takes less time to start than multi processing
2.  Threads can share data easily unlike process and have same memory heap, so to prevent threads conflicting with each other python internally use GIL
3.  Threads is there to reduce waiting time for eg. run 2 process one require input from customer and other a computational function
4.  Threads fail in case of cpu bound tasks and for any multi-core processes
5.  Threads don't execute at a time because of GIL(Global Interpreter Lock)
6.  GIL->Its there to remove deadlock b/w resources and prevent memory leaks
Multi Processing:
------------------
1.  Have one GIL per Process
2.  Can achieve truly multi-processing
3.  Harder to share data b/w processes and have separate memory space for each processes, hence no use og Global variable for processes, cause child
    process will create separate memory heap and any value updated, will be updated to the copied child processes memory heap not the parent process
    memory heap. To remove the draw back we have multiprocessing.Array, multiprocessing.value,queue.
4.  We have Lock or mutexes(same thing) that acquire lock to a shared resource so that until that resource is being released no other function can change it
    or acquire it. ex: Banking software programme with multi processing : Suppose a person has $200 and deposited 100 first and then debited $100, if it is
    without lock the a/c balance would give diff. value each time we run the program, to avoid this bug we have acquire and release
    
    
The performance of the single-threaded process and the multi-threaded process will be the almost same in python and this is because of GIL in python.
We can not achieve multithreading in python because we have global interpreter lock which restricts the threads and works as a single thread. 

Most of the time we use the multiprocessing to prevent the program from GIL. In this implementation, 
python provide a different interpreter to each process to run so in this case the single thread is provided to each process in multi-processing   
'''

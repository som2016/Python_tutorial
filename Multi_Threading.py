import threading
from threading import *
from time import sleep

def hello():
    for i in range(150):
        print('hello')

def hi():
    for i in range(150):
        print('Hi')

'''
t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hi)
t1.start()
t2.start()
'''
#t1.join()
#t2.join() This will indicate that let t1 and t2 end then execute what else left below for more better example
# watch"https://www.youtube.com/watch?v=GqHLztqy0PU"
# https://www.youtube.com/watch?v=JnFfp81VbOs

#for 2.6:
# https://stackoverflow.com/questions/849674/simple-threading-in-python-2-6-using-thread-start-new-thread
# https://www.techbeamers.com/python-multithreading-concepts/
print('____________________________________________________________________________________')
print('!!!!!!!Threading with Extending class, Multiple Class Running concurrently!!!!!')
print('____________________________________________________________________________________')

class hello1(Thread):
    def run(self):
        for i in range(150):
            print("Hello")
            sleep(1) #(1)

class hiagain(Thread):
    def run(self):
        for i in range(150):
            print('hi')
            sleep(1)#(1)

ob = hello1()
ob2 = hiagain()
'''
ob.start()
sleep(0.2) #(2)
ob2.start()

ob.join()
ob2.join()

print('Bye')
'''
# Untill this u will get collision of output like 'hellohi' or 'hihello', But Threading is working
# Now you want something like hello hi hello hi so for this use #(1)
# Now still you will see collision of two methods so for this as well use #(2)
# Now bye will overlap with run methods as when we pause both the 2 methods within that time main_thread will start exe. next line within the gap
# so for above we use:
print('____________________________________________________________________________________')
print('!!!!!!!Threading without Extending class!!!!!')
print('____________________________________________________________________________________')

class hi1:
    def myfunc(self):
        for i in range(15):
            print('Hi')

obj = hi1()
t1 = Thread(target=obj.myfunc)
t1.start()
t1.join()
print('done')



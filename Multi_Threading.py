import threading
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


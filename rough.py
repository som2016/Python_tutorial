from collections import Counter

def close(x):
    def open(x):
        p = 90
        return  x*x
    def open2(x):
        p=90
        return  x*x*x
    return open,open2

def lamp():  # This is the way I called the Inner functions
    v,v2 = close(2)
    print(close(2))
    print(v.__name__)
    print(v(3))
    print(v2(10))

lamp()

close(30)





class fun1:
    def __init__(self,x):
        self.x =x
    def output(self):
        print(self.x)

list11 = [1,2,3,4,5]
for i in list11:
    obj = fun1(i)
    obj.output()

str1 = 'Hello'
print(Counter(str1))
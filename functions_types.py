print('_________________________________________________________________________________________')
print('function A function B uses function As variable and property without touching function A')
print('_________________________________________________________________________________________')
# Note You can somehow access the values as shown below but cant able to accessparent function's inner-functions or local functions and its variables

def funA(v1, v2):
    c = v1 + v2
    print('In funA v1=', v1)
    print('In funA v2=', v2)
    print('In funA c=', c)
    return c, v1, v2  # even if we had returned multiple variable it would be stored in a list and return list


# funA(10,20)

def funB(funA):  # Note Return of funA is must otherwise it wont work
    print('In funB, Total value of funA is=', funA)
    print('In funB, funA value is=', funA[1], funA[2])
    x = funA[0]
    print('The value of c in funA=', x)


funB(funA(20, 30))

print('____________________________________________________________________________________')
print("Use Parent function Calculation in child function without modifying parent function")
print('___________________________________________________________________________________')


def funC(v1, v2):
    c = v1 + v2
    print('In funC v1=', v1)
    print('In funC v2=', v2)
    print('In funC c=', c)
    return v1, v2, c


funC(11, 9)


def funD():
    funC(2, 3)
    print('In funD funC value is=',funC)  # As we can see we can pass vars to parent but when we call the parent every time we have to provide parameters,
#    '''Hence above is impossible but if we want parent func to do any task this is how we gonna call them'''
#    print(funC[0]) #not working
#     print(funC(1,2).v1) # not working
funD()

print('____________________________________________________________________________________')
print("Use Branch or Nested Functions with return types and parameters")
print('___________________________________________________________________________________')


def funE(v1, v2):
    d = 191

    def funF():  # for this we don't need to pass v1,v2 cause these are global w.r.t funF but you can mention it result are same.
        c = v1 + v2
        print('In funF v1=', v1)
        print('In funF v2=', v2)
        print('In funF c=', c)
        print('In funF d=', d)
        return v1 * v2, c

    d = funF()
    print('In funE v1=', v1)
    print('In funE v2=', v2)
    print('In funE c=', d)  # You can't use c here as c is local for funF
    return d


funE(20, 10)
print('____________________________________________________________________________________')
print('**********************Functions returning Functions and "Recursions*****************"')

def funF(num):
    #    d = 0
    if num == 1:
        #        print('in if', d,num)
        return 1
    else:
        '''
        print('In else first', d, num)
        d = num * funF(num - 1) # Multiplication happening all at a time like 1*2,2*3,6*4,24*5, Hence d=0 5 times then after this line d increases gradually
        print('In else end', d,num)
        return d'''
        return num * funF(num-1)

# funF(5)-funF(4)-funF(3)-funF(2)funF(1)
#funF(1)=1=> funF(2)= [num(2)*funF(1)]=2 => funF(3)=> [num=3*funF(2)]=6=>funF(4)=[num=4*funF(6)]=24=>funF(5)=[num=5*funF(24)]

num = 3
print('The Factorial value is: ',funF(num))


# The refined one is as mentioned in below:


def fibbo(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibbo(num - 2) + fibbo(num - 1)  # Its a binary tree which is forming f(3) + f(2) then f3 calls f(3-1),f(3-2) againon right side f2 calls
    #f(2-1),f(2-2)... so on


num1 = 4
for i in range(num1):
#    print('ith element is:',i)
    print(fibbo(i), end=' ')
print('\n')

def recex(num):
    i = 1
    if num ==6:
        return 5
    else:
        return i + recex(num+1)

print('The recursion example value is: ',recex(0))
'''
1. i+recex(0+1) = recex(1) get called
2. i+recex(1+1) = recex(2) get called
3. i+recex(2+1) = recex(3) get called
then if num ==3 it returns value 3 to recex(2), the 3+1 =4
4=>  is the vale of recex(1) which=> 4+1 =5
now again 5 is the value for recex(0)=> 5+1 =6
now print func() is calling recex(0) which is equal to 6

func(0)-func(1)-func(2)-func(3)
fun3(5),fun2(3+1),fun1(4+1),fun0(5+1)
# Always remember the loop end point will be the if statement so if it starts from fun(0) to say if numm ==6 then
total loop=7, 7th time loop will return the return value of if so in else part whatever the calculation will be it 
will be running 6(in this case) times the return value of if
'''
print('____________________________________________________________________________________')
print('!!!!To add +1 if is odd if even then -1 for 20 numbers starting from 1(Recursion)!!!!!')
# To add +1 if is odd if even then -1 for 20 numbers starting from 1

def main1():
    num = 1
    def odd(num):
        if num<=20:
            print(num+1)
            num=num+1
            even(num)
    def even(num):
        if num<=20:
            print(num-1)
            num=num+1
            odd(num)
    odd(num)
main1()
print('____________________________________________________________________________________')
def ex2(n):

    if n==0:
       return 100
    else:
        print('Printing before return:' ,n,end=' ')
        return ex2(n-1)

ex2(3)
print('\n')
'''_______________________________________________________________________________'''
def ex3(n):
    if n==0:
        return 111
    else:
        ex3(n-1)
        print('The value after return: ', n,end=' ')
ex3(3)
print('\n')
print('____________________________________________________________________________________')
print('************Closures******************')
print('____________________________________________________________________________________')
def ex4(pow):
    def inner(x):
        print('The value of pow and x is: ', pow,x)
        return x*pow
    return inner
value = ex4(5)
print('The Multiplied value is: ',value(2))
print('___________Next Example____________________')
# So clousers are the way where we access innerfunctions beyond their normal access scope
def ex5():
    i = 21
    def inner2():
        print('Inner2 Output is:',i+1)
    print("In ex5 outer function value is:", i+2)
    return inner2
print(ex5())
v= ex5()
print('The value of v=', v.__name__) # Henc by above logic we can use inner functions which is used in the following:
#1. Use of Global variablen 2. Data Hiding
v()
print('______________________________________________________________________________________________________________')
print('!!!!!!!!!!!!!!!!How to Access Main Function"s inner Functions via other functions!!!!!!!!')
print('______________________________________________________________________________________________________________')

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


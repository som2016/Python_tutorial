print('____________________________________________________________________________________')
print('************Decorators******************')
print('____________________________________________________________________________________')


def div_mod(div):  # we can give any name instead of 'div' cause @div_mod has already been pointed to this func.
    def inner(num1, deno1):  # we had to take 2 functions cause in 1st we are passing the div function as
        # parameter the inner function is where we want to add stuff.
        if deno1 == 0 or num1 == 0:
            return '"Try again"'
        elif num1 < deno1:
            num1, deno1 = deno1, num1
            return div(num1, deno1)
        else:
            return div(num1, deno1)

    return inner


@div_mod  # Indicating a modification has been made for this 'div function' with name 'div_mod' function, but actual work is done in the inner func.
def div(num, deno):
    print('The value of Div is: ', num / deno)
    return 'in div'


print(div(2, 10))
print('____________________________________________________________________________________')
print('!!!!!!!Multiple Decorators on a single function!!!!!')
print('____________________________________________________________________________________')


def split_str1(fun):
    def inner(str1):
        temp2 = fun(
            str1)  # If we don't use temp it will overwrite with the last called decorator hence last decorator will only be actually applicable
        return temp2.split()

    return inner


def upper_str1(fun):
    def inner(str1):
        temp1 = fun(str1)
        return temp1.upper()

    return inner


# It dosn't depends on which sequence u define decorators but in which sequence u call them with @function_name
@split_str1
@upper_str1
def funS(str1):
    return str1


print(funS('Hello World!'))

print('____________________________________________________________________________________')
print('!!!!!!!Multiple Functions on a single Decorator!!!!!')
print('____________________________________________________________________________________')

def divdec(fun):
    def inner1(*args):
        list1 = []
        list1 = args
        if 0 in list1:
            return "Please Enter again"
        return fun(*args)
    return inner1
@divdec
def div1(x,y):
    return x/y
@divdec
def div2(a,b,c):
    return a/b+c

print(div1(3,3))
print(div2(6,0,4))


'''*********Remaining Map,Lamda, return overloading and overriding Functions filter reduce functions'''

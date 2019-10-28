from operator import itemgetter
import functools

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
        temp2 = fun(str1)  # If we don't use temp it will overwrite with the last called decorator
        # hence last decorator will only be actually applicable
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
def div1(x, y):
    return x / y


@divdec
def div2(a, b, c):
    return a / b + c


print(div1(3, 3))
print(div2(6, 0, 4))

print('____________________________________________________________________________________')
print('!!!!!!!Passing parameter via Decorator!!!!!')
print('____________________________________________________________________________________')


def deco_main(args):
    def outer(func):
        def inner():
            print(func())
            return func() + args

        return inner

    return outer


@deco_main('Som')
def main():
    return 'In Main: '


print(main())

# Need to know if We can able to call local functions of main function(i.e inner function of main())
# via decorated function or access its vars and vice versa
print('____________________________________________________________________________________')
print('***************Lambda Expressions/MAP/Filter/Reduce**********************************')
print('____________________________________________________________________________________')
# it is used for functions that will be used once only ex. sorting, taking input etc. also
print('!!!!!---Example-1---!!!!!')
list1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
f = (list(filter(lambda n: n % 2 == 0, list1)))
print('The Even Numbers are: ', f)

print('!!!!!---Example-2---!!!!!')

# ex = 'Som Hello'
# print(ex.strip('Hello'))
g = lambda surname, firstname: surname.strip().title() + " " + firstname.strip().title()
print(g(' som', 'das '))

print('!!!!!---Example-4--- Arrange a list of names with their titles!!!!!')

ex = ['Som Das', 'Rahul Kumar Shukla', 'Prnal Gandhi', 'Bajal Adams', 'Ashley Adams', 'Sophia leone', 'K.shukla']
ex.sort(key=lambda n: n.split(" ")[-1].lower())
print(ex)

print('!!!!!---Example-5---Work thorough each tuple elements!!!!!')
temp_list = [('Kolkata', 21), ('Delhi', 11), ('Pune', 4), ('Bangalore', 18)]
res = list(map(itemgetter(1), temp_list))
print(res)

celcius = lambda temp: (temp[0], (9 / 5) * temp[1] + 32)
print(list(map(celcius, temp_list)))
print('____________________________________________________________________________________')
'''map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
Syntax : 
if a=[a1,a2,a3..an] and f1 is the function to be applied the it will apply f@a1, f@a2..f@an
map(fun, iter)'''
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
print('____________________________________________________________________________________')
print('!!!!Checking For Palindrome!!!!!!!!')
my_list = ["geeks", "geeg", "keek", "practice", "aa", "mam"]

output = list(filter(lambda x: x == "".join(reversed(x)), my_list))
print(output)

output2 = list(filter(lambda x: x == "mam", my_list))
print(output2)
print('____________________________________________________________________________________')
lis = [1, 3, 5, 6, 2, ]
opt1 = list(map(lambda x: x + x,
                lis))  # this happening on each individual element but its a list, giving list cant be individual element.
opt2 = functools.reduce(lambda x, y: x + y,
                        lis)  # Reduce function what did is added each items in the list  and given a single output
print(opt2)

print('____________________________________________________________________________________')
print('*********************Decorators->wraps***************************')
print('____________________________________________________________________________________')


# Wraps is used to hide the original function name

def dec_main1(func):
    @functools.wraps(func)  # THis hides .__name__ from showing inner as the main function
    def inner(*args):
        list1 = args[1:]
        if 0 in list1:
            return 'Please type non-Zero Number'
        else:
            return func(*args)

    return inner


@dec_main1
def main1(x, y):
    print('The output of main1 is:', x * y)


@dec_main1
def main2(x, y, z):
    print('The output of main2 is:', x * y / z)


main1(12, 13)
main2(16, 12, 10)
print(main1.__name__)
print(main2.__name__)

print('____________________________________________________________________________________')
print('*********************classes->Decorators functions***************************')
print('____________________________________________________________________________________')


def dec_mainx(func):
    @functools.wraps(func)  # THis hides .__name__ from showing inner as the main function
    def inner(name_ref):
        list1x = name_ref.listx
        value1 = name_ref.value
        print('In inner, 2nd value is: ', value1)
        if 0 in list1x:
            print('Please type non-Zero Number')
        else:
            return func(name_ref)

    return inner


class main_hello:

    def __init__(self, *args):
        self.args = args
        self.value = 'Hello World!'

    def __call__(self):  # this will execute by default but we have to call the object as done below
        self.listx = list(self.args)

    #       print('The values in listx are: ', self.listx)

    @dec_mainx
    def main3(self):
        print('The output of main1 is:', self.listx[0] * self.listx[1])

    @dec_mainx
    def main4(self):
        print('The output of main2 is:', self.listx[0] * self.listx[1] / self.listx[2])


ob = main_hello(12, 0)
ob2 = main_hello(13, 14, 10)
ob()
ob.main3()
print(ob.main3.__name__)
ob2()
ob2.main4()

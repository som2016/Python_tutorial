import sys


def check():
    assert ('win' in sys.platform)  # , "Your text here"
    print("Hello Linux")


def divide(a, b):
    assert (b != 0), "Please no Zero"
    print(a / b)


'''Assertion is used for maainly debuging purpose and for unit tests, there are multiple assertion methods as well
like assertAlmostEqual,assertRaises,assertDictEqual etc'''
try:
    check()
    divide(10, 0)
except AssertionError as er:
    print(er)
    print("This function can only run in Linux Systems")

'''Whenever an exception is occured it is 1st handeled then code proceeds to another'''

print('______________________________________________________________________________________________________________')
print('!!!!!!!!!!!!!!!!Exception handling with Raise finally try and else!!!!!!!!')
print('______________________________________________________________________________________________________________')

import functools


def input_decor(func):
    @functools.wraps(func)
    def inner(args):
        try:
            return func(args)
        except ValueError as e1:
            print('Integer Only!!! no "String or Char" , Please try again!')
            return inner(args)
        except TypeError as e2:
            #print(e2)
            print("Number Should not be less than 0")
            return inner(args)

    return inner

def a_task_decor(func):
    @functools.wraps(func)
    def inner(args):
        try:
            return func(args)
        except TypeError as e1:
            print('Select From the Given Output and Please try again!')
            return inner(args)

    return inner

class calculator:
    def __init__(self):
        self.inputList = list()


    @input_decor
    def take_input(self):
        i = 1
        x = 0
        while True:

            if i == 1 or i == 2:
                x = (int(input('Enter %d number: ' % i)))
                if x < 0:
                    raise TypeError#("Number should not be less than 0")
                elif x > 0:
                    self.inputList.append(x)
                    i = i + 1
            else:
                check = input('Do you want to continue? Yes/No: ')
                check = check.casefold()
                if check == 'yes' or check == 'y':
                    x = (int(input('Enter %d number: ' % i)))
                    if x < 0:
                        raise TypeError  # ("Number should not be less than 0")
                    elif x > 0:
                        self.inputList.append(x)
                        i = i + 1
                elif check == 'no' or check == 'n':
                    print('Ok Exiting')
                    break
                else:
                    print('Try Again With Proper input')
    @a_task_decor
    def ask_task(self):
        print('Entered input is: ', self.inputList)
        opt = input('Enter A-add, M-multiply, D-divide,S-subtract: ')
        opt = opt.casefold()
        print(opt.isdigit())
        print(opt)
        if opt.isdigit() == 'False':
            if opt == 'a' or opt == 'add' or opt == 'addition':
                self.task_add()
            elif opt == 'm' or opt == 'multiply' or opt == 'multiplication' or opt == 'mul':
                self.task_mul()
            elif opt == 'd' or opt == 'divide' or opt == 'division' or opt == 'div':
                self.task_div()
            elif opt == 's' or opt == 'sub' or opt == 'subtract' or opt == 'subtraction':
                self.task_sub()
        else:
            print('in else')
            raise TypeError

    def task_add(self):
        print('add')

    def task_mul(self):
        print('mul')

    def task_div(self):
        print('div')

    def task_sub(self):
        print('sub')


ob = calculator()
#ob.take_input()
ob.ask_task()

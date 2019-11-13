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
        except ValueError as e1:
            print('Provided Digit instead of String hence Please try again!')
            return inner(args)
        except TypeError as e2:
            print('Please type from the Mentioned option and try again!')
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
                x = (float(input('Enter %d number: ' % i)))
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
        if not opt.isdigit():
            if opt == 'a' or opt == 'add' or opt == 'addition':
                self.task_add()
            elif opt == 'm' or opt == 'multiply' or opt == 'multiplication' or opt == 'mul':
                self.task_mul()
            elif opt == 'd' or opt == 'divide' or opt == 'division' or opt == 'div':
                self.task_div()
            elif opt == 's' or opt == 'sub' or opt == 'subtract' or opt == 'subtraction':
                self.task_sub()
            else:
                raise TypeError
        else:
            raise ValueError

    def task_add(self):
        print('add')

    def task_mul(self):
        print('mul')

    def task_div(self):
        print('div')

    def task_sub(self):
        print('sub')


ob = calculator()
ob.take_input()
ob.ask_task()

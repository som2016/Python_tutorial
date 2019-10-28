import functools


def dec_mainx(func):
    @functools.wraps(func)  # THis hides .__name__ from showing inner as the main function
    def inner(name_ref):
        list1x = name_ref.listx
        #        print('In inner, list1x value: ', list1x)
        if 0 in list1x:
            print('Please type non-Zero Number')
        else:
            return func(name_ref)

    return inner


class main_hello:

    def __init__(self, *args):
        self.args = args

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

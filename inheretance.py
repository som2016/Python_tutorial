class dev():
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2_dummyname = part2

    def movies(self):
        print('the year of part1 is: ', self.part1)
        print('the year of part2 is: ', self.part2_dummyname)


class new_rel(dev):
    movie = 'Spiderman'

    def __init__(self, part1, part2, part3):
        super().__init__(part1, part2)
        self.part3 = part3

    def movies(self):  # method over ridding
        print('the year of part1 is: ', self.part1)
        print('the year of part2 is: ', self.part2_dummyname)
        print('the year of part3 is: ', self.part3)
        print('Movie Name: ', self.movie)


obj1 = dev(2001, 2003)
obj1.movies()

obj2 = new_rel(part1=2001, part2=2003, part3=2009)
obj2.movies()

print('____________________________________________________________________________________')
print('*********************Method Resolution Oder***************************')
print('____________________________________________________________________________________')


# Python program showing
# how MRO works 

class A:
    def rk(self):
        print(" In class A")


class B(A):
    def rk(self):
        print(" In class B")


class C(A):
    def rk(self):
        print("In class C")


class S(C):
    def rk(self):
        print("In Class S")


# classes ordering
class D(S, C, B, A):
    pass


r = D()
r.rk()
print(D.mro())

# Method resolution oder > is the way you call it like K(M,n,o) so M is checked first for init after K
# also note that the subclasses should be derived first e.g C(S) as S is a sub class of C so S should be the first to get called

print('____________________________________________________________________________________')


class Dates:
    hello = 'hello'

    def __init__(self, date):
        self.date = date

    def getDate(self):
        Dates.hello = 'Welcome'
        print('Inside getData', Dates.hello)
        return self.date

    print('the class variable value outside a def', hello)

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

    @classmethod
    def clsex(cls, date):
        Dates.hello = 'Welcome'
        print('in class method', Dates.hello)
        return date.replace('/', '=')

    print('the class variable value outside a def', hello)


x = Dates.toDashDate('12/3/1991')
print(x)
x2 = Dates('30/12/2019')
print(x2.getDate())
x3 = Dates.clsex('1/1/2017')
print(x3)

''' In Static method > is used when you dont need to use class properties and hence don't need to take any
instance or class parameters. It is called without initializing a class

In Class method we have to pass a mandatory parameter called cls which mainly deals with class variables

While the default method is the instance method which take self(object) as a default parameter argument
'''


class A1:
    glob = 'Hello'

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def change1(self):
        A1.glob = 'Welcome'
        print('Inside change1', A1.glob)

    def c1(self):
        print('Inside c1', A1.glob)

    @classmethod
    def change2(cls):
        print('Inside change2', cls.glob)
        cls.glob = 'SOM'
        print('After change2', cls.glob)
        print(cls)

    def c2(self):
        print('Inside c2', A1.glob)


ob = A1(10, 20)
ob.change1()
ob.c1()
A1.change2()
ob.c2()
print('____________________________________________________________________________________')

''' Accesssors are used to fetch the data while mutators term is used where u want the change the data'''
''' Decorators in class'''


class help1:
    string = 'HelloGamers'

    def __init__(self, var1, ):
        self.var1 = var1

    def print_something(self):
        print('Hello in Help1, in print_something and var1= ', self.var1)

    # Method overloading is a feature where you can have variable no. of parameters of a same function
    def method2(self,
                string=None):  # Note: we can't use method Overloading in python but workaround is using method_name(*args)
        if string == None:
            print('No String Found')
        else:
            print('String value is:', self.var1 + string)


'''ob = help1('Camel')
ob.print_something()
ob.method2()
'''


class help2(help1):
    #    def print_something(self):   # If we directly call it without inheriting it will just call the previous func.,overriding will not work
    # and obj. had to be called in parent class or else error
    #       print('Hello in Help2')
    def __init__(self, var1, var2):
        super().__init__(var1)
        self.var2 = var2

    def print_something(self):  # In case we uncomment print_something of hel2, last fuction will override it and only last func will be shown
        print('Hello in Help2, in print_something and var1+var2= ', self.var1 + self.var2)
        print(self)


ob2 = help2('Pagal', 'Panti')
ob2.print_something()

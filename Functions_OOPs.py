def myfunction(age: object, name: object):
    print('The Age is: ', age)
    print('The name is: ', name)


myfunction(age=24, name='som')

myfunction(24, 'som')
myfunction('som', 24)


# myfunction('somqwe', age= 40)
#   myfunction(age=25, 'lastname')   #  this will give error


def myfunction2(*fruits):
    print(fruits)


#   fruits = ['apple', 'mango', 'jackfruit']
myfunction2('apple', 'mango', 'jackfruit')

'''Passing List as an Parameter into the the function'''


def abc(*b12):
    print(b2)


b2 = [1, 2, 3, 4, 5]
abc(b2)

'''-----------------------------------Itarator---------------------------------------------------------'''

l2 = [11, 22, 33, 44, 55, 66]

it = iter(l2)  # iter will give object of iterator as shown in print(it)

print(it)

print(next(it))  # Give you the next Object
print(next(it))
print(it.__next__())
print(it.__next__())

'''---------------------------Generator-------------------------------------------------------------------'''
# Generators will give iterators, it does the work of iter and next function

def gen_example():
    n =1
    while n <= 10:
        sq = n*n
        yield sq  # if you use return it will return a single value but using yield we can get the list of returns
        n += 1


v2 = gen_example()

for i in v2:
    print(i)

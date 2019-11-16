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
'''
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
'''

'''
class UnderAge(Exception):
   pass

def verify_age(age):
   if int(age) < 18:
       raise UnderAge
   else:
       print('Age: '+str(age))

# main program
verify_age(23)  # won't raise exception
verify_age(17)  # will raise exception


https://www.youtube.com/watch?v=27GrUulGrWo #Custom Exception Handling
'''
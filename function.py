def fun():
    str = "geeksforgeeks"
    x = 20
    return str, x;  # Return tuple, we could also
    # write (str, x)


# Driver code to test above method
str1, x = fun()  # Assign returned tuple < fun is returning 2 values those 2 values are getting asigned  in str and x, print directly fun()
print(fun())
print(x)
print(str1)


def fun():
    str = "geeksforgeeks"
    x = 20
    return [str, x];


# Driver code to test above method
# list1 = fun()
print(fun())

'''
class some:
    ar = 'A Variable'

    def funy(self):
        self.var = some.ar

    def __repr__(self):
        return some.ar

    def __str__(self):
        return some.ar

on2 = some()
on = some()
print(on.ar)
on.funy()
print(on.var)
print(on)
print(on2)


checklist = [1110,41,3,4,5,6,7,8,9,0,1203]
print(checklist[-1])
'''


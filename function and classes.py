print('_________________________________________________________________________________________')
print('function A function B uses function As variable and property without touching function A')
print('_________________________________________________________________________________________')


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
    print('In funD funC value is=',
          funC)  # As we can see we can pass vars to parent but when we call the parent every time we have to provide parameters,


#    '''Hence above is impossible but if we want parent func to do any task this is how we gonna call them'''

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


def funE():




'''*********Remaining Clousures, Map,Lamda and Decorator return overloading and overriding Functions'''

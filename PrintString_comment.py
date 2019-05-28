print("Hello World Statement")

'''
print("this wont be printed")
'''

a = 10
b = 20
c = 'aString'
print(a, b, c)

'''
-----------------------Lists--------------------------------
'''

list1 = [10, 22, 30, 'string1', 'string2', 'string3']
print(list1)
print(list1[0:2])
print(list1[:1])
print(list1[::-1])
print('The length of the List is:', len(list1))

'''
------------------------Dictionaries-----------------------------
'''
subjects = {'subject1': 'Maths', 'subject2': 'Physics', 'subject3': 'Chemistry'}

print(subjects)
print(subjects['subject1'])
print(len(subjects))

'''
------------------------Sets-----------------------------
'''
set1 = {1, 2, 4, 3, 3, 5, 1}
print(set1)
# Can Perform union Intersection etc. on these sets
list2 = [1, 2, 4, 3, 3, 5, 1]
print('The output of List2 is ', list2)
print('Converted into set', set(list2))

'''
------------------------Tuples-----------------------------
'''
tup1 = (11, 22, 34, 'History', 'Home')
print(tup1)
print(tup1[::-1])
print(tup1[0:4])

'''
------------------------Logical Operations-----------------------------
'''
a1 = 0
b1 = 1

print(a1 and b1)
print(a1 or b1)
print(not a1)
print(not b1)

'''
------------------------Identity Operations-----------------------------
'''

a3 = 10
b3 = 15

# noinspection PyRedundantParentheses
if (a3 is b3):
    print('a equals b')
else:
    print('a is not equal to b')

if a3 is not b3:
    print('True')
else:
    print('False')

'''
------------------------Membership Operations-----------------------------
'''
list3 = ['a', 'b', 'dig', 'egg']
if 'z' in list3:
    print('True')
else:
    print('False')
# can also use elif statements for else if
if 'digegg' not in list3:
    print('True')
else:
    print('False')

'''
------------------------While Operations-----------------------------
'''
count = 0
while (count <= 9):
    print('The current iteration is:', count)
    count = count + 1

'''
------------------------For Operations-----------------------------
'''
for i in range(1, 15 + 1, 3):  # 3 is the increment value
    print(i)
    i = i + 2

print('end')

for x in 'Somarko Das':
    print(x)

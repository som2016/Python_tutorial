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
checklist = [1,2,3,4,5,6,7,8,9,0,1203]
print(checklist[-1])

# more on basic_part2.py

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
    'i = i + 2'

print('end')

''' ----------------------------------------string to lists/array elements----------------------------------'''
array = []
for x in 'Somarko Das':
    list5 = [x]
    array.append(x)
    print(x)

print(list5)
print(array)

''' ----------------------------------- splitting ------------------------------------------------'''
word1 = 'ram is good boy'
print(word1.split())
word2 = 'ram,is,a,good,boy'
print(word2.split(','))
word3 = 'hypothetically'
print([word3[i:i + 3] for i in range(0, len(word3), 3)])
'''------------------------------------Stars-------------------------------------------------------- '''
for i in range(0, 5, 1):
    for j in range(0, i + 1, 1):
        print('*', end='')  # The end=' ' is just to say that you want a space after the end of the statement instead of a new line character.
    print('\r')

print('\r')
print('\r')

for x in range(5, 1, -1):
    for j in range(1, x, 1):
        print('*', end='')
    print('\r')

print('\r')
print('\r')

num =1
for x in range(1, 5, 1):
    for j in range(4, x, -1):
        print(' ', end='')
    for k in range(0, num, 1):
        print('*', end='')
    print('\r')
    num = num+2


for x in range(1, 5, 1):
    for j in range(4, x, -1):
        print(' ', end='')
    for k in range(1, x, 1):
        print('*', end='')
    print('\r')


list13 = [1, 2, 3, 'asd', 'bad', 'sad']
print(list13)
dict1 = {'1st': 'sub1', '2nd': 'sub2', '3rd': 'sub3'}
print(dict1['1st'])

import math

s = 1
while (s <= 5):
    print('Hello World')
    s = s + 1

word = 'One thing I dont know why it dosent even matter how hard you try keep that in mind cause i design this rhyme'

if 'why' in word:
    print('success')
else:
    print("Failed")

''' need to know check with ignore case '''

if True:
    print(
        " true executed")  # always this will be executed everytime i run the code but this will not show output infinitely
else:
    print(" false executed")

for index in range(6):  # will run from 0 to 6
    print(index)
a = 5
b = 10
c = 'Hello'
d = 'world'

# print(dir())

# x = input('docstring' )
''''this is doc string'''

x1 = 1000
print(x1, type(x1))

print(bool(0))  # False for 0 only for any other number always true

s1 = 'Python\nis\namazing'
rs1 = R'Python\nis\namazing'

s = "INfinity"
print(s.isalpha());
''' check for alphabets only in  a string'''
print(s.isdigit())
print(len(s))
print(s.lower())
print(s.count('i'))
print(s.index('t'))

v = 10.6452348
print(v.__round__(2))
'''------------------------------------------infinity---------------------------------------'''
# positive infinity
p_inf = float("inf")
# negative infinity
n_inf = float("-inf")
print(math.isinf(p_inf))
print(math.isinf(n_inf))

'''---------------Using Math Library----------------------------------------'''
# Area & Volume of a circle with 2.5 radius
r = 2.5
piv = math.pi
r2 = pow(2.5, 2)
area = 4 * r2 * piv

print(area)
r3 = pow(r, 3)
volume = (4 / 3) * piv * r3
print(volume)

'''******************LIST FUNCTIONS***************************************'''
empty_list = list()
empty_list.append(5)
print(empty_list)
empty_list.append([6, 7])
print(empty_list)  # List within a list
list2 = empty_list.pop()
print(empty_list, list2)
empty_list.extend(list2)
print(empty_list)  # merging 2 lists
empty_list.insert(0, 121)  # here 0 is the index and 121 is the value 2 b inserted
print(empty_list)
empty_list.pop(1)
print(empty_list)
print(max(empty_list))
print(min(empty_list))
print(sorted(empty_list))
empty_list.reverse()
print(empty_list)
print(empty_list.count(121))
print(empty_list.index(121))
empty_list.append(12)
empty_list.append(456)
print(len(empty_list))
print(empty_list)
empty_list.count(121)
'''-----------------------------------------------------------------------------------------------'''
k1 = range(5)
print(k1)
print(list(k1))

k2 = range(10, 15)
print(k2)
print(list(k2))

k3 = range(10, 21)
print(k3)
print(list(k3))

k4 = range(100, 1, -25)
print(list(k4))

print(max('infinity'))

count = 0
while count < 2:
    print(count, " is  less than 2")
    count = count + 2
else:
    print(count, " is not less than 2")

print(min('infinity'))


agrade = 68.3
if agrade >= 90:
    print("Distinct")
elif 60 >= agrade or agrade < 90:
    print("Above average")
elif 40 >= agrade or agrade < 60:
    print('Average')
else:
    print('Fail')

k = [3, 4, 5, 6, 7, 8, 9]
'''# Print the list of alternative numbers, using the slicing option, starting from '3'.'''
print(k[0::2])
'''Print the list of alternative numbers obtained from the first 4 elements only.'''
k2 = k[:4]
print(k2) # getting first 4 elements
print(k2[0::2])
'''Print the list of odd indexed elements of list 'k'. Since indexing starts at zero, odd indices would be 1,3, and so on.'''
print(k[1::2])
a = {10, 20, 30, 40}
b = {30,60}
u = a.union(b)
print(u)
i = a.intersection(b)
print(i)
d = a.difference(b)
print(d)
sd = a.symmetric_difference(b)
print(sd)

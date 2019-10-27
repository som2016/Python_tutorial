print(dir())
# x = input('docstring' )
# print(x)

v = 10.6452348
print(v.__round__(2))
print(int(v))
print(str(v))
list1 = list()
list1 = [1, 23, 45, 32, 11, 23, 134, 431, 23, 44]
x = list1.pop()
print('the 1', list1[:-1])
print('the 2', x)
print(list1[::-3])
print(max('infinity'))

k = [3, 4, 5, 6, 7, 8, 9]
'''# Print the list of alternative numbers, using the slicing option, starting from '3'.'''
print(k[0::2])
'''Print the list of alternative numbers obtained from the first 4 elements only.'''
k2 = k[:4]
print(k2)  # getting first 4 elements
print(k2[0::2])

l2 = [11, 22, 33, 44, 55, 66]

it = iter(l2)  # iter will give object of iterator as shown in print(it)

print(it)

print(next(it))  # Give you the next Object
print(next(it))
print(it.__next__())
print(it.__next__())



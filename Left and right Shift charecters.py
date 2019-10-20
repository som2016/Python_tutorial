str1 = 'HelloWorld'
x = int(input("Give a number for Left Shift: \n")) # by default input takes string need to convert it
leftstr = ''
liststr = list(str1)
for i in range(x):
    temp = liststr.pop(0)
    liststr.append(temp)
print('The new List is \n', liststr)
leftstr = leftstr.join(liststr)
print('The Final LeftShift is: \n', leftstr)

str2 = 'HappyWorld'
x2 = int(input("Give a number for Right shift: \n"))
rightstr = ""
liststr2 = list(str2)
for i in range(x2):
    temp2 = liststr2.pop()
    liststr2.insert(0,temp2)
print('The new LeftShift List is: \n', liststr2)
rightstr= rightstr.join(liststr2)
print('The Final leftShift is: \n', rightstr)
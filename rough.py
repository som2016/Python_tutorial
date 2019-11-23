import sys
import re

xlist, xlistF = [], []

MyList = ["New York", "London", "Paris", "New Delhi"]

MyFile = open('output.txt', 'w')
MyList = map(lambda x: x + '\n', MyList)
MyFile.writelines(MyList)
MyFile.close()

#! /usr/bin/python3
import re
from datetime import datetime
import functools
import sys
import multiprocessing

xlist, xlistF = [], []

# This Structure helps to get a single point of exception handling for all the below functions
def exception_handling(func):
    @functools.wraps(func)
    def inner():
        try:
            return func()
        except FileNotFoundError as er:
            print('No Such File Found, Please Try Again!!!')
        except IndexError as er2:
            print("Please Enter File Path while Running the Script")

    return inner


@exception_handling
def file_read():
    filepath = sys.argv[1]  # To catch External Vars passed while running the script. We start with [1] cause it takes the .py script itself as argument [0]
    fp = open(filepath, 'r')
    for line in fp:
        if re.search("localhost.com:", line):
            temp = re.sub('[\n: \t]', '', line)
        elif re.search("Failed", line):
            xlist.append(temp) if '0' in line else xlistF.append(temp)
    fp.close()
    sort_list(xlist, xlistF)
    if __name__ == '__main__':
        p1,p2 = multiprocessing.Process(target=out_puts),multiprocessing.Process(target=out_putf)
        p1.start(),p2.start(),p1.join(),p2.join()

def sort_list(xlist, xlistF):
    global listS, listF
    xlist, listF = list(dict.fromkeys(xlist)), list(dict.fromkeys(xlistF)) #Removing Duplicates
    listS = (list(set(xlist).difference(set(xlistF)))) # Removing any Success minions which are there in failed list

def out_puts():
    sfile = open('Success_Log--' + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"), 'w')
    for line in listS:
        sfile.write(line),sfile.write("\n")
    sfile.close()


def out_putf():
    xfile = open('Failed_Log--' + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"), 'w')
    if not listF:
        xfile.write('Nothing Failed')
    else:
        for line in listS:
            xfile.write(line),xfile.write("\n")
    xfile.close()

file_read()


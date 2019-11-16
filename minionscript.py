#! /usr/bin/python3
import re
from datetime import datetime

xlist, xlistF = [], []


def file_read():
    try:
        filepath = "F:\\Training Programs\\Python\\xestfile.txt"
        fp = open(filepath, 'r')
        for line in fp:
            if re.search("localhost.com:", line):
                temp = re.sub('[\n: \t]', '', line)
            elif re.search("Failed", line):
                if '0' in line:
                    xlist.append(temp)
                else:
                    xlistF.append(temp)
        fp.close()
        sort_list(xlist, xlistF),out_puts(),out_putf()
    except FileNotFoundError as er:
        print('No Such File Found Try Again!!!')
    except Exception as er2:
        print("Hello")


def sort_list(xlist, xlistF):
    global listS, listF
    xlist, listF = list(dict.fromkeys(xlist)), list(dict.fromkeys(xlistF))
    listS = (list(set(xlist).difference(set(xlistF))))


def out_puts():
    print('----------SUCCESS-----------')
    sfile = open('Success_Log--' + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"), 'w')
    for line in listS:
        print(line)
        sfile.write(line)
        sfile.write("\n")
    sfile.close()


def out_putf():
    print('----------FAILED-----------')
    xfile = open('Failed_Log--' + datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p"), 'w')
    if not listF:
        print('Nothing Failed')
        xfile.write('Nothing Failed')
    else:
        for line in listS:
            print(line)
            xfile.write(line)
            xfile.write("\n")
    xfile.close()


file_read()

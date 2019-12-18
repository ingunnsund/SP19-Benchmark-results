#!/usr/bin/env python

def calculate(filename):
    f = open(filename, 'r')

    content = f.read()
    lines = content.splitlines()
    newList = []

    for line in lines:
        if 'float' in line:
            firstPart, secondPart = line.split('float',1)
            newList.append(int(secondPart.strip()))
            
    totalVal = 0
    for element in newList: 
        totalVal += element

    print(filename)
    print(totalVal)

calculate('rtx-infer-float-notc')
calculate('rtx-infer-float-tc')
print('--')
calculate('ms-infer-float-notc')
calculate('ms-infer-float-tc')
print('--')
calculate('yme-infer-float-notc')
calculate('yme-infer-float-tc')
print('--')
calculate('dgx2-infer-float-notc')
calculate('dgx2-infer-float-tc')
print('--')
calculate('gtx-infer-float')

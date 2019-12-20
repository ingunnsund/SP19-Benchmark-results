#!/usr/bin/env python

def calculate(filename, conv=False):
    f = open(filename, 'r')

    content = f.read()
    lines = content.splitlines()
    newList = []

    for line in lines:
        if 'float' in line:
            firstPart, secondPart = line.split('float',1)
            newList.append(int(secondPart.strip()))
        if 'int8' in line:
            firstPart, secondPart = line.split('int8',1)
            if conv:
                fPart, sPart = secondPart.split('IMPLICIT_PRECOMP_GEMM', 1)
                newList.append(int(fPart[:-5].strip()))
            else:
                newList.append(int(secondPart[:-1].strip()))
    totalVal = 0
    for element in newList: 
        totalVal += element

    print(filename)
    print(totalVal)

"""
print('------------------------Infer')
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

print('------------------------Train')
calculate('rtx-train-float-notc')
calculate('rtx-train-float-tc')
print('--')
calculate('ms-train-float-notc')
calculate('ms-train-float-tc')
print('--')
calculate('yme-train-float-notc')
calculate('yme-train-float-tc')
print('--')
calculate('dgx2-train-float-notc')
calculate('dgx2-train-float-tc')
print('--')
calculate('gtx-train-float')
"""

calculate('dgx2-infer-int8-notc')
calculate('dgx2-infer-int8-tc')

calculate('rtx-infer-int8-notc')
calculate('rtx-infer-int8-tc')

calculate('yme-infer-int8-notc')
calculate('yme-infer-int8-tc')

calculate('ms-infer-int8-notc')
calculate('ms-infer-int8-tc')

print('-----CONV-----')

calculate('CONV-yme-infer-int8-notc', True)
print('67/107')
calculate('CONV-yme-infer-int8-tc', True)
print('81/107')

calculate('CONV-dgx2-infer-int8-notc', True)
calculate('CONV-dgx2-infer-int8-tc', True)

calculate('CONV-rtx-infer-int8-notc', True)
calculate('CONV-rtx-infer-int8-tc', True)

calculate('CONV-ms-infer-int8-notc', True)
calculate('CONV-ms-infer-int8-tc', True)
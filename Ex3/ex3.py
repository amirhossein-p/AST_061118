import numpy as np
import math
from decimal import Decimal

def fn1(n):
    outF = []
    for i in range(n):
        outF.append(str(2*i))
    return outF

def fn2(n):
    outF = []
    for i in range(n):
        outF.append('{0:.4f}'.format(i**0.5))
    return outF

def fn3(n):
    outF = []
    for i in range(n):
        num = 10**i
        outF.append('%.2E' % Decimal(num))
    return outF

def fn4(n):
    outF = []
    for i in range(n):
        outF.append(str(i**3))
    return outF

def fn5(n):
    outF = []
    for i in range(n):
        try:
            outF.append('{0:.4f}'.format(2**(1/i)))
        except:
            outF.append('None')
    return outF

def fn6(n):
    outF = []
    for i in range(n):
        num = math.exp(i)
        outF.append('%.2E' % Decimal(num))
    return outF

if __name__ == '__main__':
    n = 100
    no = np.array(np.arange(100))[np.newaxis].T
    f1 = np.array(fn1(n))[np.newaxis].T
    f2 = np.array(fn2(n))[np.newaxis].T
    f3 = np.array(fn3(n))[np.newaxis].T
    f4 = np.array(fn4(n))[np.newaxis].T
    f5 = np.array(fn5(n))[np.newaxis].T
    f6 = np.array(fn6(n))[np.newaxis].T
    data = np.hstack([no, f1, f2, f3, f4, f5, f6])

    names = ['No.', '2n', 'n^0.5', '10^n', 'n^3', '2^(1/n)', 'e^n']
    lines = ['---', '------', '------', '------', '------', '------', '------']

    row_format ="{:>15}" * (len(names) + 1)
    print(row_format.format("", *names))
    print(row_format.format("", *lines))
    for i in range(len(data[:,1])):
        print(row_format.format("", *data[i,:]))

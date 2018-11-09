import numpy as np

def calcSum(inList):
    return np.sum(inList)

def calcProduct(inList):
    return np.prod(inList)

def calcAverage(inList):
    return np.average(inList)

def calcVariance(inList):
    return np.var(inList)

def calcMin(inList):
    return np.min(inList)

def calcMax(inList):
    return np.max(inList)

if __name__ == '__main__':
    noOfInputds = 0
    inList = []
    while(True):
        noOfInputds = int(input('Enter number of integers: '))
        if (noOfInputds < 100) and (noOfInputds > 0) :
            break
        else:
            print('Please enter number between 1 & 100!')

    for i in range(int(noOfInputds)):
        inList.append(int(input('Enter integer ')))
    print('sum = ',calcSum(inList))
    print('product = ', calcProduct(inList))
    print('average = ', calcAverage(inList))
    print('variance = ', calcVariance(inList))
    print('min = ', calcMin(inList))
    print('max = ', calcMax(inList))

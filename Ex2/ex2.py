import numpy as np

def calcPrime():
    primes = []
    for i in range(2, 100):
        isPrime = True
        for j in range(2,i):
            if (i % j == 0):
                isPrime = False
        if(isPrime):
            primes.append(i)
    return primes

if __name__ == '__main__':
    calcPrime()

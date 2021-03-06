import numpy as np
import time

def calcPrime(n):
    t = time.time()
    primes = [2,3]
    for i in range(2, n):
        isPrime = True
        for j in primes:
            if (i % j == 0):
                isPrime = False
        if(isPrime):
            primes.append(i)
    return primes , (time.time() - t)

if __name__ == '__main__':
    prList1 = []
    tim1 = 0.0
    prList1 , tim1 = calcPrime(1000)
    prList2 = []
    tim2 = 0.0
    prList2 , tim2 = calcPrime(10000)
    print('Elapsed time for calculating prime numbers 0 - 1000:', tim1)
    print('Elapsed time for calculating prime numbers 0 - 10000:', tim2)

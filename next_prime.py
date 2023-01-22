from is_prime_number import isPrimeNumber
def nextPrime(a):
    n = a + 1
    while(True):
        if (isPrimeNumber(n)):
            return n
        n = n + 1

# print(nextPrime(7))
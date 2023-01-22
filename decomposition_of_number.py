from is_prime_number import isPrimeNumber
from next_prime import nextPrime

def decompositionOfNumber(a, prime = 2, primeFactors = []):
    if( a == prime ):
        primeFactors.append(prime)
        return primeFactors
    if(a%prime == 0):
        primeFactors.append(prime)
        return decompositionOfNumber( a/prime, 2, primeFactors)
    return decompositionOfNumber( a, nextPrime(prime), primeFactors)

# print(decompositionOfNumber(48))
# using trial division

from math import sqrt
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
	
# Tests....
print isPrime(3) # Should output True
print isPrime(143) # Should output False
print isPrime(790003) # Should output True
print isPrime(2) #True
print isPrime(1) #false
print isPrime(0) #false
print isPrime(4) #False
print isPrime(5) #True
print isPrime(9) #False
print isPrime(11) #True
print isPrime(20) #False

import math
n = int(input())
primes = []
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(*primes)        
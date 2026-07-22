import math
n = int(input())
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.isqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
if is_prime(n):
    print("TUB")
else:
    print("TUB EMAS")
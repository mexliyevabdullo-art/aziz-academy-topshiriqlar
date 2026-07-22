import math
n = int(input())
if n <= 1:
    print("MUKAMMAL EMAS")
else:
    divisors_sum = 1
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                divisors_sum += i
            else:
                divisors_sum += i + (n // i)
    if divisors_sum == n:
        print("MUKAMMAL")
    else:
        print("MUKAMMAL EMAS")
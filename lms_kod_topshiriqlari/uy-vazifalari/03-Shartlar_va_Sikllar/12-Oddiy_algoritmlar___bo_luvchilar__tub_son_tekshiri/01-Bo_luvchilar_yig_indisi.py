import math
n = int(input())
total_sum = 0
for i in range(1, int(math.isqrt(n)) + 1):
    if n % i == 0:
        if i * i == n:
            total_sum += i
        else:
            total_sum += i + (n // i)
print(total_sum)        
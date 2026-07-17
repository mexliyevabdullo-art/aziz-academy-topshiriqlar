n = int(input())
while n >= 10: 
    yigindi = 0
    while n > 0:
        yigindi += n % 10
        n = n // 10
    n = yigindi
print(n)    
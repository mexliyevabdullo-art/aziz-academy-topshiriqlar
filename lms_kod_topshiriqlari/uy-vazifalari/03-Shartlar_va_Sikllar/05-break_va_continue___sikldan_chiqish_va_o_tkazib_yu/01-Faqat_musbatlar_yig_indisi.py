n = int(input())
yigindi = 0
i = 0
while i < n:
    son = int(input())
    i += 1
    if son <= 0:
        continue
    yigindi += son 
print(yigindi)    
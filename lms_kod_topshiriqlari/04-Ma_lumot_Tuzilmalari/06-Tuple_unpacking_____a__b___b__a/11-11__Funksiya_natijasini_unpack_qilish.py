def calc(a, b):
    return a + b, a * b
x, y = map(int, input().split())
sum_val, prod_val = calc(x, y)
print(sum_val)
print(prod_val)
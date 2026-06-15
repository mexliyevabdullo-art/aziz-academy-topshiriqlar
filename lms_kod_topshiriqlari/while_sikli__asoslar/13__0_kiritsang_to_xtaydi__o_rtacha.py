s = c = 0

while(x := int(input())):
    s += x
    c += 1
print(0 if s == 0 else s / c)

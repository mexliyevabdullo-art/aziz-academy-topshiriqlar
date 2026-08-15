import sys
i = map(int, sys.stdin.read().split())
while (o := next(i)) != 0:
    a, b = next(i), next(i)
    print(a+b if o==1 else a-b if o==2 else a*b if o==3 else "Xato" if b==0 else a//b if 0==4 else "Noma'lum")
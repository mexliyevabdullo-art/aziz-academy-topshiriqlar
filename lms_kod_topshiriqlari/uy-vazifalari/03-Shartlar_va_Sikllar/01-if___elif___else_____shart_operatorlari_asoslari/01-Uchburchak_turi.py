a = int(input())
b = int(input())
c = int(input())
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + b <= b or b + c <= a:
    print("notogri")
elif a == b == c:
    print("teng tomonli")
elif a == b or a == c or b == c:
    print("teng yonli")
else:
    print("turli tomonli")
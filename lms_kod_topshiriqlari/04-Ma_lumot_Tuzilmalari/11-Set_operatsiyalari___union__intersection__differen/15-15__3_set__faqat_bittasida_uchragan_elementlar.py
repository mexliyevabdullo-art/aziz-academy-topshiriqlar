A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
result = (A ^ B ^ C) - (A & B) | (B & C) | (A & B)
all_alements = A | B | C 
result = set()
for x in all_alements:
    count = (x in A) + (x in B) + (x in C)
    if count == 1:
        result.add(x)
if result:
    print(*(sorted(result)))
else:
    print("BO'SH")
A = set(input().strip().split())
B = set(input().strip().split())
common = A & B 
print(len(common))
for name in sorted(common):
    print(name)
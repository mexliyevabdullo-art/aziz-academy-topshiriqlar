ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
try:
    _ = input()
except EOFError:
    pass
allowed = ids - banned
if allowed:
    print(*(sorted(allowed)))
else:
    print("BO'SH")
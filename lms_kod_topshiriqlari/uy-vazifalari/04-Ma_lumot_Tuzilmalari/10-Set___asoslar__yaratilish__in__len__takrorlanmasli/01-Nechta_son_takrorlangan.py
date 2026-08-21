seen = set()
dups = set()
for son in input().split():
    if son in seen:
        dups.add(son)
    else:
        seen.add(son)
print(len(dups))        
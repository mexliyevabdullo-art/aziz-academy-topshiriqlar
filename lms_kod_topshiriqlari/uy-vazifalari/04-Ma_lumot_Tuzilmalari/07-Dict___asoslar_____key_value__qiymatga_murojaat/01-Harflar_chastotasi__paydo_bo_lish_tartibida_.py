s = input()
for c in dict.fromkeys(s):
    print(c, s.count(c))
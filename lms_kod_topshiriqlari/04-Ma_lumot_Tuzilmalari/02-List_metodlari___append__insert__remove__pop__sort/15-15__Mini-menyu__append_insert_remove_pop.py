lst = []
while True:
    a = input().split()
    if a[0] == "stop":
        break
    elif a[0] == "append":
        lst.append(int(a[1]))
    elif a[0] == "insert":
        lst.insert(int(a[1]), int(a[2]))
    elif a[0] == "remove":
        if int(a[1]) in lst:
            lst.remove(int(a[1]))
    elif a[0] == "pop":
        lst.pop(int(a[1]))
print(lst)        
            
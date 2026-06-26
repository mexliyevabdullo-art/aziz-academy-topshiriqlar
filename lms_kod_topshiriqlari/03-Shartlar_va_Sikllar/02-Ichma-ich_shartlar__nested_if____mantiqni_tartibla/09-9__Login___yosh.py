login, yosh = input().split()
yosh = int(yosh)

if login == "admin":
    if yosh >= 18:
        print("Full access")

else:
    print("No access")
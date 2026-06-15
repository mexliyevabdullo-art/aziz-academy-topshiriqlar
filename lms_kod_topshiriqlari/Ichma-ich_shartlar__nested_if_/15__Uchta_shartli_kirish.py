login, status = input().split()
status = int(status)
if login == "admin":
    if status == 1:
        print("Admin active")
    else:
        print("Admin inactive")
else:
    print("User")
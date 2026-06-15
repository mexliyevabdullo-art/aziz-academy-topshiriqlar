role = input()
print("Full access" if role == "admin" else "Limrtrd" if role == "user" else "Guest")
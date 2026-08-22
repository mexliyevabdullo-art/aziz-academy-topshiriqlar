# INPUT:
# n
# n qator: username k tag1 ... tagk
# Vazifa: eng ko‘p tagga ega userni chiqaring: username
# Agar teng bo‘lsa: birinchi uchragani.

n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})

# TODO
best_user = max(users, key=lambda x: len(x['tags']))
print(best_user['username'])
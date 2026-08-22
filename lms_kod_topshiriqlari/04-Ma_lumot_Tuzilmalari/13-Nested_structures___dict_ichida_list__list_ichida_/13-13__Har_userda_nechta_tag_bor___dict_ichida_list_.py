# INPUT:
# n
# n qator: username k tag1 tag2 ... tagk
# Vazifa: har user uchun taglar sonini chiqaring.
# Output: username son
# (Input tartibida)

n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})

# TODO
for user in users:
    print(user['username'], len(user['tags']))
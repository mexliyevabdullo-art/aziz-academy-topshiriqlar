# INPUT:
# n
# n qator: username k tag1 ... tagk
# Vazifa: hamma userlar bo‘yicha unikal taglar sonini chiqaring.

n = int(input().strip())
users = []
for _ in range(n):
    parts = input().split()
    username = parts[0]
    k = int(parts[1])
    tags = parts[2:2+k]
    users.append({'username': username, 'tags': tags})

# TODO
print(len({tag for user in users for tag in user['tags']}))
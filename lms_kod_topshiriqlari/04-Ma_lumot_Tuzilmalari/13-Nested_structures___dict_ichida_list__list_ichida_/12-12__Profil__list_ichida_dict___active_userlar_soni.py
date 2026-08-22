# INPUT:
# n
# n qator: username active
# active: 1 yoki 0
# Vazifa: active=1 bo‘lganlar soni

n = int(input().strip())
users = []
for _ in range(n):
    username, active = input().split()
    users.append({'username': username, 'active': active == '1'})

# TODO
active_count = 0 
for user in users:
    if user['active']:
        active_count += 1 
print(active_count)        
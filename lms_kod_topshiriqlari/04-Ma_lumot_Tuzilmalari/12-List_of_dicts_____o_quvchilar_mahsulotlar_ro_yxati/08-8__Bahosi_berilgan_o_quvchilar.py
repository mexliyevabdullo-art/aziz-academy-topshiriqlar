# N ta o‘quvchi
# Keyin bitta son X
# Bahosi X ga teng bo‘lganlar sonini chiqaring

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
x = int(input())
# TODO
count = sum(1 for s in students if s['score'] == x)
print(count)
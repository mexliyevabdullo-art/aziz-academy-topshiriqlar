# N ta o‘quvchi
# Bahosi 80 dan katta bo‘lganlar sonini chiqaring

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
count = sum(1 for s in students if s['score'] > 80)
print(count)
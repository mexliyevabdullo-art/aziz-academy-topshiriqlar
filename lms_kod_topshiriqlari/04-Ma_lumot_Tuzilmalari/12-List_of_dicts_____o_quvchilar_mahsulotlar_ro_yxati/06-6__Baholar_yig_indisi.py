# N ta o‘quvchi
# Barcha baholar yig‘indisini chiqaring

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
total_score = sum(s['score'] for s in students)
print(total_score)
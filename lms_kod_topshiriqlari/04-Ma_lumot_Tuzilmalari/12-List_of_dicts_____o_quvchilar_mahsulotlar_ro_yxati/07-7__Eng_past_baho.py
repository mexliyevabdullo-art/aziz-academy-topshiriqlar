# N ta o‘quvchi
# Eng kichik bahoni chiqaring

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
min_score = min(s['score'] for s in students)
print(min_score)
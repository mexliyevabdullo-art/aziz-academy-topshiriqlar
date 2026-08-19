# N ta o‘quvchi
# Eng katta bahoni chiqaring

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
max_score = max(student['score'] for student in students)
print(max_score)
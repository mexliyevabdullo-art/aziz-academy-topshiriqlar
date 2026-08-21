# INPUT:
# n
# n qator: course_name k student1 ... studentk
# Vazifa: eng ko‘p o‘quvchili kurs nomini chiqaring.
# Agar teng bo‘lsa: birinchi uchragan kursni chiqaring.

n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': name, 'students': students})

# TODO
best_course = max(data['courses'], key=lambda x: len(x['students']))
print(best_course['name'])
# INPUT:
# 1-qator: n (kurslar soni)
# Keyingi n qator: course_name k student1 student2 ... studentk
# Vazifa: jami kurslar sonini chiqaring (n)

n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    course_name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': course_name, 'students': students})

# TODO: natija
print(n)
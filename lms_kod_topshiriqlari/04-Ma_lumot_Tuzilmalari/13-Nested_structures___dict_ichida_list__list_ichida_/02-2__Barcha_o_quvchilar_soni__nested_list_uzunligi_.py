# INPUT:
# 1-qator: n (kurslar soni)
# Keyingi n qator: course_name k student1 ... studentk
# Vazifa: hamma kurslar bo‘yicha jami o‘quvchilar sonini chiqaring

n = int(input().strip())
data = {'courses': []}
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    data['courses'].append({'name': name, 'students': students})

# TODO
total_students = sum(len(course['students']) for course in data['courses'])
print(total_students)
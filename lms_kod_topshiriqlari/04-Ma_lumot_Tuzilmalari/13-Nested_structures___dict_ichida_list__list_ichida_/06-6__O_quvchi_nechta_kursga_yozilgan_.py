# INPUT:
# n
# n qator: course_name k student1 ... studentk
# oxirgi qator: student_name
# Vazifa: student_name nechta kursda qatnashishini chiqaring.

n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})

student = input().strip()
# TODO
count = 0
for course in courses:
    if student in course['students']:
        count += 1
print(count)        
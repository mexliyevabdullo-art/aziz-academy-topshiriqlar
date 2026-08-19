
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
total_score = sum(student['score'] for student in students)
average_score = total_score / n if n > 0 else 0 
print(average_score)
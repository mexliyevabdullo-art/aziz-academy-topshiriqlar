import sys
lines = sys.stdin.read().splitlines()
students = []
for line in lines[1:]:
    parts = line.split()
    students.append({
        "name": parts[0],
        "grades": [int(x) for x in parts[1:]]
    })
max_grade = -1
best_name = ""
for s in students:
    for g in s["grades"]:
        if g > max_grade:
            max_grade = g 
            best_name = s["name"]
print(f"{best_name} {max_grade}")            
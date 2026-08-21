n = int(input())
students = []
for _ in range(n):
    data = input().split()
    name = data[0]
    age = int(data[1])
    students.append({"name": name, "abe": age})
for s in students:
    print(s["name"])
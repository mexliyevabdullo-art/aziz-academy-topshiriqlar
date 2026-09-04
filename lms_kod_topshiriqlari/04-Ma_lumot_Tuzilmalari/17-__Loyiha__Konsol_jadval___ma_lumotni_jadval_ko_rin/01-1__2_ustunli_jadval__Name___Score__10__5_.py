n = int(input())
print("Name       | Score")
print("-" * 10 + "+-----")
for _ in range(n):
    name, score = input().split()
    print(f"{name:<10} | {int(score):>5}")
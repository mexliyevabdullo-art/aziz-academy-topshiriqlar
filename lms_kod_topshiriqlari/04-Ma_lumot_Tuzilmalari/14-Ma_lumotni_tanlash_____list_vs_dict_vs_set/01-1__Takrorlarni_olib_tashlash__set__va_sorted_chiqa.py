numbers = map(int, input().split())
unique_sorted = sorted(set(numbers))
print(*unique_sorted)
a, b, c, d = map(int, input().split())
result = (a + b*2) - (c//2) + (d%3)
if result == 9:
    print(f"Result: {result-1}")
elif result == 12:
    print(f"Result: {result+1}")
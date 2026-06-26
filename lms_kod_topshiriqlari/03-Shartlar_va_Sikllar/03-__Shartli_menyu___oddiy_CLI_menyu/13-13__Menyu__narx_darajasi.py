price = int(input())
print("Cheap" if price < 50 else "Medium" if price < 200 else "Expensive")
weather = input().strip()
print({"sunny": "Go out", "rainiy": "Stay home"}.get(weather, "Unknown"))
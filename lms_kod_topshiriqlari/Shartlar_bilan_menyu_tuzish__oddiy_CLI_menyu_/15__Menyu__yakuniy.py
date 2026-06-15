choice = input().strip()
print({"start": "Started", "stop": "Stopped", "pause": "Paused"}.get(choice, "Unknown command"))
import sys
input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    sozlar = input_data[1:]
    nat = [x for x in sozlar if len(x) >= n]
    print(nat)
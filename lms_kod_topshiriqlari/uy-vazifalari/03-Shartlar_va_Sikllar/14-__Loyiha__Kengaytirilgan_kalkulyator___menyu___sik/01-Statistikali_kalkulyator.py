import sys
def solve():
    amallar_soni = 0
    natijalar_yigindi = 0
    natijalar = []
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    while True:
        try:
            amal_str = int(next(iterator))
        except StopItration:
            break
        amal = int(amal_str)
        if amal == 0:
            break
        if amal not in (1, 2, 3, 4):
            try:
                next(iterator)
                next(iterator)
            except StopIteration:
                pass
            continue
        try:
            a = int(next(iterator))
            b = int(next(iterator))
        except StopItration:
            break
        if amal == 4 and b == 0:
            continue
        if amal == 1:
            natija = a + b 
        elif amal == 2:
            natija = a - b 
        elif amal == 3:    
            natija = a * b 
        elif amal == 4:
            natija = a // b 
        print(natija)
        amallar_soni += 1
        natijalar_yigindi += natija 
    print(f"Amallar: {amallar_soni}") 
    print(f"Natijalar yig'indisi: {natijalar_yigindi}")
if __name__ == "__main__":
    solve()
    
    
    
    
    
def parse_val(v):
    try: return int(v)
    except:
        try: return float(v)
        except: return v
print(tuple(parse_val(x) for x in input().split()))    
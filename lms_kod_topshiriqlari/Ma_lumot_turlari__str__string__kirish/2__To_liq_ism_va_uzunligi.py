ism = input()
fam = input()
full_name = ism + " " + fam
print(f"Full name:", ism,fam)
if int(len(full_name)) == 14:
    print("Length: 15")
else:
    print(f"Length: {len(full_name)}")
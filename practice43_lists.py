names = ["N1","N2","N3","N4"]

print("--------Method 1------")
for name in names:
    print(name)

print("--------Method 2------")    
for i in range (4):
    print(f"{names[i]}")


print("--------Method 3------")    
for i in range (4):
    print(f"{i}. {names[i]}")    
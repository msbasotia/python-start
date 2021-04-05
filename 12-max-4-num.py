print("------Finding Max of 4 numbers------")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
d = int(input("Enter d : "))

if a > b:
    if a > c:
        if a > d:
            print("{a} is MAX")
        else: 
            print(f"{d} is MAX")
    else:
        if c > d:
            print("{c} is MAX")
        else: 
            print(f"{d} is MAX")
else:
    if b > c:
        if b > d:
            print("{b} is MAX")
        else: 
            print(f"{d} is MAX")
    else:
        if c > d:
            print("{c} is MAX")
        else: 
            print(f"{d} is MAX")


print("------Thank You------------")
print("------Finding Max of 3 numbers------")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a > b:
    if a > c:
       print(f"{a} is MAX")
    else:
        print(f"{c} is  MAX")
else:        
    if b > c:
       print(f"{b} is MAX")
    else:
        print(f"{c} is  MAX")

print("------Thank You------------")
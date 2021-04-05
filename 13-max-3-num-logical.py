print("------Finding Max of 3 numbers------")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a > b and a > c:
    print(f"{a} is max")
elif b > a and b > c:
    print(f"{b} is max")    
else:
    print(f"{c} is max")    

    
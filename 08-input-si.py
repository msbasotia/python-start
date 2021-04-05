print("-----------Simple Interest Calculation------------")


p = float(input("Enter the principle amount : "))
t = int(input("Enter the years : "))
r = float(input("Enter the interest rate : "))

si = p * t * r / 100 # formula can be called only after variables have been declared

print(f"Simple Interest is {si} ")
print(f"You will get back {p+si} ")

print(f"-------THANK YOU--------")
a=15
b=2

#addition
print(str(a) + " + " + str(b) + " = " + str(a+b))
print(a,"+",b,"=",a+b)
print(f"{a} + {b} = {a+b}") #this looks the best and easy to use
print("{} + {} = {}".format(a,b,a+b))
print("{x} + {y} = {arith}".format(x=a,y=b,arith=a+b))

#subtraction
print(f"{a} - {b} = {a-b}")

#multiplication
print(f"{a} * {b} = {a*b}")

#division
print(f"{a} / {b} = {a/b}")

#quotient
print(f"{a} // {b} = {a//b}")

#remainder
print(f"{a} % {b} = {a%b}")
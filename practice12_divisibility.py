def divisibility(n,x):
    if n % x == 0:
        print(f"{n} is divisible by {x}")
    else:
        print(f"{n} is not divisible by {x}")


def main():
    n = int(input("Enter number to check : "))
    divisibility(n,5)
    divisibility(n,11)


main()
def count_digits(n):

    custom_n = n
    digits = 1
    while custom_n // 10 > 0:
        digits = digits + 1
        custom_n = custom_n // 10
    print(f"The number of digits in {n} is {digits}")




def main():
    n = int(input("Enter value of n : "))
    count_digits(n)

main()    


# is this the reason we use while loop? (we can give custom conditions)
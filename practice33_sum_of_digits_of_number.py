def count_digits(n):

    custom_n = n
    digits = 1
    while custom_n // 10 > 0:
        digits = digits + 1
        custom_n = custom_n // 10
    return digits

def sum_digits(n):
    s = 0
    i = 1
    custom_n = n      
    """ it is necessary to declare custom_n as we need a variable whose value keeps changing
      and at same time we need a FIXED value for count_digits() function """
    while i <= (count_digits(n)):     
        s = s + (custom_n % 10)
        custom_n = custom_n // 10
        i = i+1
    return s


def main():
    n = int(input("Enter value of n : "))
    print(f"Sum of digits of {n} is {sum_digits(n)}.")
    # print(count_digits(n))


main()    
def last(n):
    l = n % 10
    return l

def count_digits(n):

    custom_n = n
    digits = 1
    while custom_n // 10 > 0:
        digits = digits + 1
        custom_n = custom_n // 10
    return digits

def power(n):
    i = 1
    multi = 1
    while i <= count_digits(n)-1:
        multi = 10*multi
        i = i+1
    return multi

def first(n):
    f = n // power(n)
    return f


def main():
    n = int(input("Enter the value of n : "))
    print(f"The first and last digits of {n} are {first(n)} and {last(n)} respectively.")

main()    


# is there any way to find power of a number easily instead of putting a loop?
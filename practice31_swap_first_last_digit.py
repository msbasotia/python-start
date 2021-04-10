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

def mid_section(n):
    g = (n % power(n)) // 10
    return g

def main():
    n = int(input("Enter the value of n : "))
    print(f"After swapping the first and last digits of {n} the number becomes {last(n)}{mid_section(n)}{first(n)}.")
    # print(last(n))
    # print(count_digits(n))
    # print(power(n))
    # print(first(n))
    # print(mid_section(n))

main()    

# code is not working for numbers which have 0 at 2nd position. for eg - 300456
# solution in v2
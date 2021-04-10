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

def new_num(n):
    y = last(n)*power(n)
    y = y + (n % power(n))
    y = y - last(n)
    y = y + first(n)
    return y

# logic from https://codeforwin.org/2016/01/c-program-to-swap-first-and-last-digit-of-number.html    

def main():
    n = int(input("Enter the value of n : "))
    print(f"After swapping the first and last digits of {n} the number becomes {new_num(n)}.")


    # print(last(n))
    # print(count_digits(n))
    # print(power(n))
    # print(first(n))
    # print(new_num(n))

main()    

def count_digits(n):
    custom_n = n
    digits = 1
    while custom_n // 10 > 0:
        digits = digits + 1
        custom_n = custom_n // 10
    return digits


def power(n):
    p = 1
    for i in range (1,n):
        p = p * 10
    return p

def reverse(n):
    custom_n = n
    i = 1
    rev = 0
    while i <= count_digits(n):
        x = custom_n % 10
        rev = rev + ( power(count_digits(n)-i+1) * x )
        custom_n = custom_n // 10
        i = i+1
    return rev

# logic used from https://codeforwin.org/2015/06/c-program-to-find-reverse-of-any-number.html


def main():
    n = int(input("Enter value of n : "))
    print(f"The reverse of {n} is {reverse(n)}")
    if n == reverse(n):
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is NOT a palindrome")

main()    



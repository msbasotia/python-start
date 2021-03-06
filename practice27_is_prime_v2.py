def is_prime(n):
    sum = 0
    i = 2
    while i <= n-1:
        if n % i == 0:
            sum = sum+i
        i = i+1
    return sum

# by using this logic you would running the complete the loop for multiple times, even if you get the answer in 1st iteration.
# Hence use a return statement

def is_prime_status(n):
    if is_prime(n) == 0:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a not prime number")

def main():
    is_prime_status(5)
    is_prime_status(10)
    is_prime_status(13)
    is_prime_status(18)


main()
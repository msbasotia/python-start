def is_prime(n):
    i = 2
    while i <= n-1:
        if n % i == 0:
            return False
        i = i+1
    return True



def is_prime_status(n):
    if is_prime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a not prime number")

def main():
    is_prime_status(5)
    is_prime_status(10)
    is_prime_status(13)
    is_prime_status(18)


main()
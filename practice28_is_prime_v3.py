def is_prime(n):
    sum = 0
    i = 2
    while i <= n-1:
        if n % i == 0:
            sum = sum+i
        i = i+1
    if sum == 0:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a not prime number")


def main():
    is_prime(5)
    is_prime(10)
    is_prime(13)
    is_prime(18)


main()
def is_perfect(n):
    sum = 0
    i = 1
    while i < n:
        if n % i == 0:
            sum = sum + i
        i = i + 1

    return n == sum


def main():
    i = 1
    while i <= 10000:
        if is_perfect(i):
            print(i)
        i = i + 1


main()

#computation took a lot of time. any shorter method?
def fact(n):
    x = 1
    for i in range (1,n+1):
        x = x * i
    return x

def is_strong(n):
    i = n
    y = 0
    while i > 0:
        x = i % 10
        y = fact(x) + y
        i = i // 10

    return n == y


def main():
    i = 1
    while i <= 10000:
        if is_strong(i):
            print(i)
        i = i + 1


main()
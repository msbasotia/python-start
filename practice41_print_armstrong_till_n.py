def is_arm_strong(n):
    i = n
    y = 0
    while i > 0:
        x = i % 10
        y = x*x*x + y
        i = i // 10

    return n == y


def main():
    i = 1
    while i <= 10000:
        if is_arm_strong(i):
            print(i)
        i = i + 1


main()
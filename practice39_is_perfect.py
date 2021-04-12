

def is_perfect(n):
    sum = 0
    i = 1
    while i < n:
        if n % i == 0:
            sum = sum + i
        i = i + 1

    return n == sum


def main():
    print("-----Is Strong-----")
    print(f"6 ------> {is_perfect(6)}")
    print(f"28 ------> {is_perfect(28)}")
    print(f"496 ------> {is_perfect(496)}")
    print(f"8128 ------> {is_perfect(8128)}")
    print(f"50 ------> {is_perfect(50)}")
    print(f"1024 ------> {is_perfect(1024)}")

main()
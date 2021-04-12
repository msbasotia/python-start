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
    print("-----Is Strong-----")
    print(f"145 ------> {is_strong(145)}")
    print(f"2 ------> {is_strong(2)}")
    print(f"370 ------> {is_strong(370)}")

main()
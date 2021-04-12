

def is_arm_strong(n):
    i = n
    y = 0
    while i > 0:
        x = i % 10
        y = x*x*x + y
        i = i // 10

    return n == y


def main():
    print("-----Is Strong-----")
    print(f"371 ------> {is_arm_strong(371)}")
    print(f"407 ------> {is_arm_strong(407)}")
    print(f"28 ------> {is_arm_strong(28)}")

main()
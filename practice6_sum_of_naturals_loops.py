
# def get_sum(n):
#     sum = 0
#     for i in range(n+1):
#         sum = sum + i
#     print(f"Sum of first {n} naturals is {sum}")


# def main():
#     n = int(input("Enter the value of n : "))
#     get_sum(n)

# main()    



# When we want to call the sum into another function we have to return the value


def get_sum(n):
    s = 0
    for i in range(n+1):
        s = s + i
    return s


def main():
    n = int(input("Enter the value of n : "))
    sum = get_sum(n)
    print(f"Sum of first {n} naturals is {sum}")

main()    
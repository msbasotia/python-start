


def print_sum(num):
    sum = int((num*(num+1))/2)
    print(f"sum of  first {num} natural numbers is {sum}")


def main():
    n = int(input("Enter value of n : "))
    print_sum(n)


main()    
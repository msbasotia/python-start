def space(n):
    i = n
    while i >= 1:
        print(" ", end = "")
        i = i-1


def print_star_ends():
    i = 1
    while i <= 10:
        print("* ",end = "")
        i = i+1
    print()


def print_star_first():
    print("*",end = "")

def print_star_end():
    print("*")    


def main():
    space(9)
    print_star_ends()
    i = 1
    while i <= 8:
        space(10-i-1)
        print_star_first()
        space(17)
        print_star_end()
        i = i+1
    print_star_ends()


main()
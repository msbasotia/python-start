
def print_line(n):
    for i in range(n):
        print("*",end = "")

    print()


def main():
    for i in range(5,0,-1):
        print_line(i)

main()        
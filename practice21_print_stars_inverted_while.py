def print_star(n):
    i = 1
    while i <= n:
        print("*",end = "")
        i = i+1
    print()

def main():
    i = 10
    while i >= 1:
        print_star(i)
        i = i-1

main()        
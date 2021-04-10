def sums(n):
    i = 1
    sum = 0 
    while i <= n:
        sum = sum+i*i
        i = i+1
    
    print(f"sum of square of first {n} natural numbers is {sum}")


def main():
    sums(5)
    sums(10)
    sums(13)
    sums(96)

main()
def get_sum(n):
    s = 0
    for i in range(n+1):
        s = s + i*i*i
    return s

def main():
    n = int(input("Enter value of n : "))
    sum = get_sum(n)
    print(f"Sum of cubes of first {n} natural numbers is {sum}")


main()    

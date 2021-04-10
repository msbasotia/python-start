# def sums(n):
#     i = 1
#     sum = 0 
#     while i <= n:
#         sum = sum+i
#         i = i+1
#     return sum


# def main():
#     print(f"sum of first 5 natural numbers is {sums(5)}")
#     print(f"sum of first 10 natural numbers is {sums(10)}")
#     print(f"sum of first 13 natural numbers is {sums(13)}")
#     print(f"sum of first 96 natural numbers is {sums(96)}")


# main()    


# or we can write the programme as

def sums(n):
    i = 1
    sum = 0 
    while i <= n:
        sum = sum+i
        i = i+1
    
    print(f"sum of first {n} natural numbers is {sum}")


def main():
    sums(5)
    sums(10)
    sums(13)
    sums(96)

main()    

